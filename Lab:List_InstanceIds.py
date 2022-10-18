import boto3

client=boto3.client("ec2")
x = client.describe_instances()


for reservation in x["Reservations"]:
    for instance in reservation["Instances"]:
        print(instance['InstanceId'])
    