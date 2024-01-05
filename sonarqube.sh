#!/bin/bash

# Define environment variables
SONAR_HOST_URL="http://sonarqube:9000"
SONAR_PROJECT_KEY="my-project-key"
SONAR_TOKEN="my-token"

# Check if SonarQube is running
while ! curl -s -o /dev/null -w "%{http_code}" "${SONAR_HOST_URL}"; do
  echo "Waiting for SonarQube to start..."
  sleep 1
done

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
