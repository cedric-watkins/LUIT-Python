import boto3
import os
import glob

# #upload single file
# s3_resource = boto3.client("s3")
# s3_resource.upload_file(
#     Filename = "upload.png",
#     Bucket = "bucketnamegohere",
#     Key = "uploadtest.png"
#     )
    
#upload multiple files
cwd=os.getcwd()
cwd=cwd+"/pictures/"
print(f"This is the current working directory:\n {cwd}")

files=glob.glob(cwd+"*.png")
print(f"\nThese are the file found:\n{files}")

for file in files:
    s3_resource = boto3.client("s3")
    s3_resource.upload_file(
    Filename = file,
    Bucket = "bucketnamegohere",
    Key = file.split("/")[-1]
    )