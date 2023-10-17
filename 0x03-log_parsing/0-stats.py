import sys
import signal

total_file_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

def signal_handler(sig, frame):
    print_metrics()
    sys.exit(0)

def print_metrics():
    print(f"Total file size: {total_file_size}")
    for status_code in sorted(status_code_counts.keys()):
        if status_code_counts[status_code] > 0:
            print(f"{status_code}: {status_code_counts[status_code]}")

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()

        import re
        match = re.match(r'^(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$', line)
        if not match:
            continue

        ip_address, status_code, file_size = match.groups()

        total_file_size += int(file_size)
        status_code = int(status_code)
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    print_metrics()