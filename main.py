import boto3
import os
import logging
from botocore.exceptions import ClientError

access_key = os.getenv('accesskeyid')  #Need access key and id 
access_secret = os.environ.get('accesskeysecret')
region = 'us-east-1'
# logger congig
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

createbucketconfiguration = {'LocationConstraint': region}

# Step 1 funcion to create S3 bucket and upload an image from your local drive to it

def create_bucket(s3_client,bucket_name,image_name):
    try:
        if region == 'us-east-1':
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=createbucketconfiguration)
        s3_client.upload_file("C:/Users/venka/image/level4.jpg", bucket_name, image_name)

    except ClientError:
        logger.exception(f'Could not create bucket - {bucket_name}')
        raise



# Step 2 make call to function to create bucket and upload an image to it from local computer

if __name__=='__main__':
    bucket_name = 'testvenbucket12356'  # make sure you pick a unique bucket name
    image_name = 'test.jpg'  # name you want to give uploaded image to S3 bucket
    s3_client = boto3.client('s3', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=access_secret)
    create_bucket(s3_client,bucket_name,image_name)

# Step 3 to generate a presigned url for the bucket photo
    url = s3_client.generate_presigned_url(ClientMethod='get_object', Params={'Bucket': bucket_name, 'Key': image_name}, ExpiresIn=3600)
    print(url)
