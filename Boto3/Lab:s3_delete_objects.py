import boto3

s3_resource=boto3.client("s3")

#delete single object
# s3_resource.delete_object(
#     Bucket="bucketnamegohere",
#     Key="objectname")

#delete multiple objects
#find all the objects in the bucket
objects=s3_resource.list_objects(Bucket="bucketnamegohere")["Contents"]
print("Objects being deleted:")

for object in objects:
    print(object["Key"])
    response = s3_resource.delete_object(
        Bucket="bucketnamegohere",
        Key=object["Key"]
        )
    print(response)
    
    