#!/bin/bash

# Script to run multiple commands

# Run tests
echo -e "Running tests... \n"
coverage run -m unittest discover -v
echo -e "\n\n"
# Run coverage
echo "Running coverage..."
coverage report -m
echo -e "\n\n"
# Any additional commands you want to run
# ...

echo "All commands executed successfully."
