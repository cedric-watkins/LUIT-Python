import boto3

aws_resource = boto3.resource("s3")
bucket = aws_resource.Bucket("bucketnamegoherealsotoo")
response = bucket.create(
    ACL = "private",
    CreateBucketConfiguration={
        'LocationConstraint':'us-east-2'
    }
    
)

print(response)