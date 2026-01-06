import boto3
import json

s3 = boto3.client("s3")
response = s3.list_buckets()
buckets = response["Buckets"]

i = 0
for bucket in buckets:
    print(f"{i}: {bucket["Name"]}")
    i += 1