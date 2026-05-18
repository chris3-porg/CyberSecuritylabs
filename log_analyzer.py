import re
from collections import Counter

def analyze_log(filename):
    failed_logins = []
    ip_addresses = []
    errors = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                if 'FAILED' in line or 'failed' in line:
                    failed_logins.append(line.strip())

                ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
                if ip:
                    ip_addresses.extend(ip)

                if 'ERROR' in line or 'error' in line:
                    errors.append(line.strip())

        print("\n--- LOG ANALYSIS REPORT ---")
        print(f"Total Failed Logins: {len(failed_logins)}")
        print(f"Total Errors Found: {len(errors)}")

        if ip_addresses:
            print("\nTop 5 IP Addresses:")
            ip_count = Counter(ip_addresses)
            for ip, count in ip_count.most_common(5):
                print(f"  {ip} — {count} times")

        if failed_logins:
            print("\nFailed Login Attempts:")
            for login in failed_logins:
                print(f"  {login}")

        if errors:
            print("\nErrors Detected:")
            for error in errors:
                print(f"  {error}")

        print("\n--- END OF REPORT ---")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

filename = input("Enter log file name: ")
analyze_log(filename)