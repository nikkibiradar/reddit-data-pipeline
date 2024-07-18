# pipeline to upload data into aws s3

import s3fs
from utils.constants import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

# connecting to s3
def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(anon=False,
                               key=AWS_ACCESS_KEY_ID,
                               secret=AWS_SECRET_ACCESS_KEY)
        print("Connected to S3")
        return s3
    except Exception as e:
        print(e)

def create_bucket_if_not_exists(s3: s3fs.S3FileSystem, bucket: str):
    try:
        if not s3.exists(bucket):
            s3.mkdir(bucket)                #creating a bucket
            print("Bucket created")
        else:
            print("Bucket already exists")
    except Exception as e:
        print(e)

def upload_to_s3(s3: s3fs.S3FileSystem, file_path: str, bucket:str, s3_file_name:str):
    try:
        print(f"Uploading file from {file_path} to {bucket}/raw/{s3_file_name}")
        s3.put(file_path, bucket+'/raw/'+ s3_file_name)     # (file path that you putting from, destination path you're putting at)
        print("FIle uploaded to S3 successfully")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(e)
