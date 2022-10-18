import boto3 

#Call the "ec2" resource with boto3 to make and send request to our ec2 services
ec2_resource = boto3.resource("ec2", region_name="us-east-1")

# filters for "running" instances with the Environment:Dev tag associated with them and stores them into a variable called "Instances"
instances = ec2_resource.instances.filter(
    Filters = [
        {'Name': 'instance-state-name', 'Values': ['running']},
        {'Name': 'tag:Environment', 'Values':['Dev']}
            ]
    )


#Stops the "running" instances filtered out by the "Environment:Dev" tag
for instance in instances:
    if instance in instances:
        instance.stop()
        print(f'{instance} successfully stopped')
        
print("All other Instances are still in their original state")