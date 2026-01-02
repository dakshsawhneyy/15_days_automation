#!/bin/bash

set -euo pipefail

WEBSITE=""

while getopts "s:" opt; do
    case $opt in
        s) WEBSITE="$OPTARG" ;;
        ?) echo "Script Usage: ./script <website>"; exit 1;;
    esac
done
 
if [ -z "$WEBSITE" ]; then
    echo "Script Usage: ./script <website>"
    exit 1
fi

STATUS_CODE=$(curl -Is --max-time 5 -o /dev/null -w "%{http_code}" "$WEBSITE")

if [[ $STATUS_CODE -eq 200 ]]; then
    echo "$WEBSITE is online [STATUS_CODE: $STATUS_CODE]"
else
    echo "$WEBSITE is offline [STATUS_CODE: $STATUS_CODE]"
fi