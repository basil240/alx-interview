import sys
import re
from collections import defaultdict

line_count = 0
total_size = 0
status_counts = defaultdict(int)
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

try:
    for line in sys.stdin:
        line = line.strip()
        line_count += 1

        match = re.match(r'.*HTTP/1.1" (\d+) (\d+)$', line)
        if match:
            status_code, file_size = int(match.group(1)), int(match.group(2))
            total_size += file_size
            if status_code in status_codes:
                status_counts[status_code] += 1

        if line_count % 10 == 0:
            print(f"Total file size: {total_size}")
            for code in sorted(status_counts.keys()):
                print(f"{code}: {status_counts[code]}")


print(f"Total file size: {total_size}")
for code in sorted(status_counts.keys()):
    print(f"{code}: {status_counts[code}")