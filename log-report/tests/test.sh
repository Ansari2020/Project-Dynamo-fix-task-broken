#!/bin/bash

# Ensure the required verifier directory exists
mkdir -p /logs/verifier

# Run pytest using the correct --ctrf flag
# We use '|| true' so the script doesn't exit immediately on test failure
pytest /tests/test_outputs.py -rA --ctrf /logs/verifier/ctrf.json
EXIT_CODE=$?

# Write the final score based on the test result
if [ $EXIT_CODE -eq 0 ]; then
  echo "1" > /logs/verifier/reward.txt
else
  echo "0" > /logs/verifier/reward.txt
fi