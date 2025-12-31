#!/bin/bash

# Log Generator
# for i in {1..1000}; do
#     echo "192.168.1.$((RANDOM % 20)) - - [$(date)] \"GET / HTTP/1.1\" $((RANDOM % 5 == 0 ? 500 : 200))" >> access.log
# done

LOG_FILE="$(dirname "$0")/access.log"

awk '$NF == "500" {ips[$1]++} END {for (ip in ips) print ips[ip], ip}' $LOG_FILE | sort -nr