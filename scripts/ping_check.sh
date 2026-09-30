#!/bin/bash
# ping_check.sh - checks whether each host in hosts.txt is reachable

HOSTS_FILE="hosts.txt"
REPORT="ping_report.txt"

echo "Ping report - $(date)" > "$REPORT"

while read -r host; do
  [ -z "$host" ] && continue
  if ping -c 2 -W 2 "$host" > /dev/null 2>&1; then
    echo "$host: UP" | tee -a "$REPORT"
  else
    echo "$host: DOWN" | tee -a "$REPORT"
  fi
done < "$HOSTS_FILE"
