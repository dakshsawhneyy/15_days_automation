#!/bin/bash

LOG_FILE="$(dirname "$0")/access.log"
WORKSPACE="/var/lib/jenkins/workspace"

# awk '$6 == "Failed" {ips[$11]++} END {for (ip in ips) print ips[ip], ip}' $LOG_FILE | sort -nr

# find $WORKSPACE -type f -name "*.tmp" -size +100M -mtime +7 -exec rm -rf {} \

awk '$9 == "404" {ips[$1]++} END {for (ip in ips) print ips[ip],ip}' | sort -nr | head -n 5