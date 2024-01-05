#!/bin/bash

# Define environment variables
SONAR_HOST_URL="http://localhost:9000"
SONAR_PROJECT_KEY="my-project-key"
SONAR_TOKEN="my-token"

# Check if SonarQube is running
while ! curl -s -o /dev/null -w "%{http_code}" "${SONAR_HOST_URL}"; do
  echo "Waiting for SonarQube to start..."
  sleep 1
done

# Check for existing SonarQube Scanner installation
if ! command -v sonar-scanner &> /dev/null; then
  # Download and install the appropriate version
  echo "Installing SonarQube Scanner..."
  curl -O https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.7.0.2747-linux.zip  # Adjust for your OS
  unzip sonar-scanner-cli-4.7.0.2747-linux.zip  # Adjust for your OS
  mv sonar-scanner-4.7.0.2747-linux /opt/sonar-scanner  # Adjust for your preference
  export PATH=$PATH:/opt/sonar-scanner/bin  # Adjust for your preference
fi

# Check compatibility between SonarQube Server and Scanner
echo "Checking SonarQube Server version..."
SERVER_VERSION=$(curl -s -o /dev/null -w "%{http_code}" "${SONAR_HOST_URL}")
if [[ $SERVER_VERSION -eq 200 ]]; then
  SERVER_VERSION=$(curl -s "${SONAR_HOST_URL}/api/server/version")
  SCANNER_VERSION=$(sonar-scanner --version | grep "Version" | cut -d' ' -f2)
  if [[ "$SERVER_VERSION" != "$SCANNER_VERSION" ]]; then
    echo "WARNING: Server version ($SERVER_VERSION) and Scanner version ($SCANNER_VERSION) differ. Potential compatibility issues."
  fi
else
  echo "ERROR: Unable to check SonarQube Server version. Please ensure it's running."
  exit 1
fi

# Create a project
curl -X POST "${SONAR_HOST_URL}/api/projects" -H "Content-Type: application/json" -d '{
  "name": "My Project",
  "projectKey": "${SONAR_PROJECT_KEY}"
}'

# Create a token
curl -X POST "${SONAR_HOST_URL}/api/users/me/tokens" -H "Content-Type: application/json" -d '{
  "name": "My Token",
  "scopes": ["project:read", "project:write"]
}'

# Get the token
TOKEN=$(curl -X GET "${SONAR_HOST_URL}/api/users/me/tokens" -H "Authorization: Bearer ${SONAR_TOKEN}")

# Send the code to be analyzed
sonar-scanner \
  --sonar-host-url="${SONAR_HOST_URL}" \
  --sonar-project-key="${SONAR_PROJECT_KEY}" \
  --sonar-login="${TOKEN}" \
  --sonar-sources=.
