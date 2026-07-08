import json
import re
from collections import Counter

paths, ips, total = Counter(), set(), 0
with open("/app/access.log") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        total += 1
        ips.add(line.split()[0])
        m = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
        if m:
            paths[m.group(1)] += 1

# Take the top 3 most common pages and turn them into a dictionary
popular = dict(paths.most_common(3))

with open("/app/report.json", "w") as out:
    json.dump(
        {
            "total_requests": total,
            "unique_clients": len(ips),
            "popular_pages": popular,
        },
        out,
    )
print("wrote /app/report.json")