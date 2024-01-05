#!/bin/bash

# Script to run multiple commands in one go
# command: ./security.sh

# Run code security tests
set -e
echo -e "Scanning for vulnerabilities... \n"
bandit -r ./src/
echo -e "\n\n"
# Run dependencies security tests
echo "Scanning dependencies vulnerabilities..."
safety check
echo -e "\n\n"

echo "All commands executed successfully."
