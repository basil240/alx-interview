#!/usr/bin/python3
import sys
from collections import defaultdict

def process_line(line, metrics):
    try:
        parts = line.split()
        if len(parts) != 10 or parts[5] != "GET":
            # Skip lines with incorrect format
            return

        status_code = int(parts[8])
        file_size = int(parts[9])

        metrics['total_size'] += file_size
        metrics['status_codes'][status_code] += 1

    except (ValueError, IndexError):
        # Skip lines with incorrect or missing values
        pass

def print_metrics(metrics):
    print(f"Total file size: {metrics['total_size']}")
    print("Number of lines by status code:")
    
    # Print status codes in ascending order
    for status_code in sorted(metrics['status_codes']):
        count = metrics['status_codes'][status_code]
        print(f"{status_code}: {count}")

def main():
    metrics = {'total_size': 0, 'status_codes': defaultdict(int)}
    line_count = 0

    try:
        for line in sys.stdin:
            process_line(line.strip(), metrics)
            line_count += 1

            if line_count % 10 == 0:
                print_metrics(metrics)
    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        print_metrics(metrics)

if __name__ == "__main__":
    main()