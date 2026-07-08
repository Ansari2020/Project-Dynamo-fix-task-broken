# Parse Access Log to JSON Report

An HTTP server access log is provided at `/app/access.log`. Analyze the network traffic log and generate a structured summary report.

### Success Criteria:
1. Parse every valid request log line from `/app/access.log`.
2. Generate a JSON report saved exactly at the absolute path `/app/report.json`.
3. The schema of `/app/report.json` must strictly contain these keys:
    - `"total_requests"`: (integer) Total number of request lines.
    - `"unique_clients"`: (integer) Total number of distinct client IP addresses.
    - `"popular_pages"`: (object) Top 3 most frequently requested URLs mapped to their request counts.