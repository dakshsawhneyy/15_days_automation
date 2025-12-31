#!/bin/bash

set -euo pipefail

LOGS_DIR="$(dirname "$0")/logs_test"

if [ ! -d "$LOGS_DIR" ]; then
    echo "Not a valid directory"
    exit 1
fi

while read -r file; do
    filename=$(basename $file)
    echo "Compressing File $filename"
    gzip "$file"
done < <(find $LOGS_DIR -type f -name "*.log")