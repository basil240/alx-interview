import sys
import re
from collections import defaultdict

log_format = r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)'

total_file_size = 0
status_code_counts = defaultdict(int)

line_count = 0

try:
    for line in sys.stdin:
        match = re.match(log_format, line)
        if match:
            line_count += 1
            ip, date, status_code, file_size = match.groups()
            total_file_size += int(file_size)
            status_code_counts[status_code] += 1

            if line_count % 10 == 0:
                print("Total file size: File size:", total_file_size)
                for code in sorted(status_code_counts):
                    if code in ['200', '301', '400', '401', '403', '404', '405', '500']:
                        print(f"{code}: {status_code_counts[code]}")
        
except KeyboardInterrupt:
    print("Keyboard interruption received. Printing current statistics:")
    print("Total file size: File size:", total_file_size)
    for code in sorted(status_code_counts):
        if code in ['200', '301', '400', '401', '403', '404', '405', '500']:
            print(f"{code}: {status_code_counts[code]}")