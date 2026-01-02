#!/bin/bash

LOG_FILE="$(dirname "$0")/access.log"
WORKSPACE="/var/lib/jenkins/workspace"

# awk '$6 == "Failed" {ips[$11]++} END {for (ip in ips) print ips[ip], ip}' $LOG_FILE | sort -nr

# find $WORKSPACE -type f -name "*.tmp" -size +100M -mtime +7 -exec rm -rf {} \

# awk '$9 == "404" {ips[$1]++} END {for (ip in ips) print ips[ip],ip}' | sort -nr | head -n 5

ps -aux | awk '{print $3, $2, $NF}' | sort -nr | head -n 5

while read -r file; do
    basename=$(basename $file)
    size=$(du -h $file)

    echo "$basename, $size"
done < <(find /var/log -type f -exec sort -nr \; -exec head -n 5 \;)