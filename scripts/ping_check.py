#!/usr/bin/env python3
"""ping_check.py - checks whether each host in hosts.txt is reachable."""
import subprocess
from datetime import datetime


def is_reachable(host):
    """Return True if the host answers a ping."""
    result = subprocess.run(
        ["ping", "-c", "2", "-W", "2", host],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0


def read_hosts(path):
    """Read one host per line, skipping blank lines."""
    with open(path) as f:
        return [line.strip() for line in f if line.strip()]


def main():
    hosts = read_hosts("hosts.txt")
    report = [f"Ping report - {datetime.now()}"]
    for host in hosts:
        status = "UP" if is_reachable(host) else "DOWN"
        line = f"{host}: {status}"
        print(line)
        report.append(line)
    with open("ping_report.txt", "w") as f:
        f.write("\n".join(report) + "\n")


if __name__ == "__main__":
    main()

