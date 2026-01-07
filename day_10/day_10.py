import boto3
import json

# Ticket 1
# s3 = boto3.client("s3")
# response = s3.list_buckets()
# buckets = response["Buckets"]

# for i, bucket in enumerate(buckets):
#     print(f"{i}: {bucket["Name"]}")
    

# Ticket 2
ec2 = boto3.client("ec2")
response = ec2.describe_instances()
instances = response["Reservations"]
for instance in instances:
    inst = instance["Instances"]
    for ins in inst:
        instance_id = ins["InstanceId"]
        state = ins["State"]["Name"]
        
        print(f"ID: {instance_id} | State: {state}")
    
# dakshsawhneyy@StormBreaker:/mnt/c/Studies/DevOps/15_days_automation/day_10$ python3 day_10.py 
# [{'ReservationId': 'r-0036f4733d64f22a2', 'OwnerId': '897722695334', 'Groups': [], 'Instances': [{'Architecture': 'x86_64', 'BlockDeviceMappings': [{'DeviceName': '/dev/sda1', 'Ebs': {'AttachTime': datetime.datetime(2025, 12, 23, 10, 7, 49, tzinfo=tzlocal()), 'DeleteOnTermination': True, 'Status': 'attached', 'VolumeId': 'vol-08ee70c21bb9c39cf'}}], 'ClientToken': 'c7ac8c9d-7e7b-400f-9ccb-6d1d7491766d', 'EbsOptimized': False, 'EnaSupport': True, 'Hypervisor': 'xen', 'NetworkInterfaces': [{'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': 'ec2-65-2-80-247.ap-south-1.compute.amazonaws.com', 'PublicIp': '65.2.80.247'}, 'Attachment': {'AttachTime': datetime.datetime(2025, 12, 23, 10, 7, 48, tzinfo=tzlocal()), 'AttachmentId': 'eni-attach-07193aea94a55f3a0', 'DeleteOnTermination': True, 'DeviceIndex': 0, 'Status': 'attached', 'NetworkCardIndex': 0}, 'Description': '', 'Groups': [{'GroupId': 'sg-046b37ece9a716989', 'GroupName': 'launch-wizard-9'}], 'Ipv6Addresses': [], 'MacAddress': '0a:c0:00:d3:04:39', 'NetworkInterfaceId': 'eni-0a0c94c16e38b3495', 'OwnerId': '897722695334', 'PrivateDnsName': 'ip-172-31-3-16.ap-south-1.compute.internal', 'PrivateIpAddress': '172.31.3.16', 'PrivateIpAddresses': [{'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': 'ec2-65-2-80-247.ap-south-1.compute.amazonaws.com', 'PublicIp': '65.2.80.247'}, 'Primary': True, 'PrivateDnsName': 'ip-172-31-3-16.ap-south-1.compute.internal', 'PrivateIpAddress': '172.31.3.16'}], 'SourceDestCheck': True, 'Status': 'in-use', 'SubnetId': 'subnet-075d5e6f00b1896b7', 'VpcId': 'vpc-09ee39c452e7277dc', 'InterfaceType': 'interface', 'Operator': {'Managed': False}}], 'RootDeviceName': '/dev/sda1', 'RootDeviceType': 'ebs', 'SecurityGroups': [{'GroupId': 'sg-046b37ece9a716989', 'GroupName': 'launch-wizard-9'}], 'SourceDestCheck': True, 'Tags': [{'Key': 'Name', 'Value': 'hello'}], 'VirtualizationType': 'hvm', 'CpuOptions': {'CoreCount': 1, 'ThreadsPerCore': 1}, 'CapacityReservationSpecification': {'CapacityReservationPreference': 'open'}, 'HibernationOptions': {'Configured': False}, 'MetadataOptions': {'State': 'applied', 'HttpTokens': 'required', 'HttpPutResponseHopLimit': 2, 'HttpEndpoint': 'enabled', 'HttpProtocolIpv6': 'disabled', 'InstanceMetadataTags': 'disabled'}, 'EnclaveOptions': {'Enabled': False}, 'BootMode': 'uefi-preferred', 'PlatformDetails': 'Linux/UNIX', 'UsageOperation': 'RunInstances', 'UsageOperationUpdateTime': datetime.datetime(2025, 12, 23, 10, 7, 48, tzinfo=tzlocal()), 'PrivateDnsNameOptions': {'HostnameType': 'ip-name', 'EnableResourceNameDnsARecord': True, 'EnableResourceNameDnsAAAARecord': False}, 'MaintenanceOptions': {'AutoRecovery': 'default', 'RebootMigration': 'default'}, 'CurrentInstanceBootMode': 'legacy-bios', 'NetworkPerformanceOptions': {'BandwidthWeighting': 'default'}, 'Operator': {'Managed': False}, 'InstanceId': 'i-054529d958b431abe', 'ImageId': 'ami-02b8269d5e85954ef', 'State': {'Code': 16, 'Name': 'running'}, 'PrivateDnsName': 'ip-172-31-3-16.ap-south-1.compute.internal', 'PublicDnsName': 'ec2-65-2-80-247.ap-south-1.compute.amazonaws.com', 'StateTransitionReason': '', 'KeyName': 'general-key-pair', 'AmiLaunchIndex': 0, 'ProductCodes': [], 'InstanceType': 't2.micro', 'LaunchTime': datetime.datetime(2025, 12, 23, 10, 7, 48, tzinfo=tzlocal()), 'Placement': {'AvailabilityZoneId': 'aps1-az3', 'GroupName': '', 'Tenancy': 'default', 'AvailabilityZone': 'ap-south-1b'}, 'Monitoring': {'State': 'disabled'}, 'SubnetId': 'subnet-075d5e6f00b1896b7', 'VpcId': 'vpc-09ee39c452e7277dc', 'PrivateIpAddress': '172.31.3.16', 'PublicIpAddress': '65.2.80.247'}]}]
# dakshsawhneyy@StormBreaker:/mnt/c/Studies/DevOps/15_days_automation/day_10$ 