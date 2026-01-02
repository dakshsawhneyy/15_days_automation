#!/bin/bash

if ! curl -Is -w "%{http_code}" -o /dev/null --max-time 5 www.google.com ; then
    echo "Offline"
else
    echo "200 OK -- "Online""
fi

nc -zv -w 2 8.8.8.8:443