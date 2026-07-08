import json
import pytest
from pathlib import Path

# Path to the agent's output
OUTPUT_FILE = Path("/app/report.json")

def test_report_exists():
    """Verifies that the agent created the output file at /app/report.json."""
    assert OUTPUT_FILE.exists(), "The report.json file was not created in /app/."

def test_report_contents():
    """Verifies that report.json contains the required keys and valid data types."""
    with open(OUTPUT_FILE) as f:
        data = json.load(f)

    # Check for required keys
    assert "total_requests" in data, "Missing required key: total_requests"
    assert "unique_clients" in data, "Missing required key: unique_clients"
    assert "popular_pages" in data, "Missing required key: popular_pages"

    # Check data types
    assert isinstance(data["total_requests"], int), "total_requests must be an integer"
    assert isinstance(data["unique_clients"], int), "unique_clients must be an integer"
    assert isinstance(data["popular_pages"], dict), "popular_pages must be a dictionary"

def test_popular_pages_limit():
    """Verifies that the popular_pages dictionary contains no more than 3 entries."""
    with open(OUTPUT_FILE) as f:
        data = json.load(f)

    assert len(data["popular_pages"]) <= 3, "popular_pages contains more than 3 entries"