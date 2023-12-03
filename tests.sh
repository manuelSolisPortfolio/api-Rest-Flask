#!/bin/bash

# Script to run multiple commands in one go
# command: ./tests.sh

# Run tests
echo -e "Running tests... \n"
coverage run -m unittest discover -v
echo -e "\n\n"
# Run coverage
echo "Running coverage..."
coverage report -m
echo -e "\n\n"

echo "All commands executed successfully."
