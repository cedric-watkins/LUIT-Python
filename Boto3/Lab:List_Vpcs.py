import boto3


resource = boto3.client("ec2")

x = resource.describe_vpcs()
num_of_vpcs = x["Vpcs"]
#print(num_of_vpcs)

for vpc in num_of_vpcs:
    print(vpc["VpcId"])
