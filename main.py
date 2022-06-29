import urllib
from urllib import response
import boto3
import json

s3 = boto3.client('s3')


def lambda_handler(event, context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    target_bucket = 'my-student-output-data'
    copy_source = {'Bucket': source_bucket, 'Key': object_key}

    try:
        print(object_key)
        print("Using waiter to waiting for object to persist through s3 service")
        waiter = s3.get_waiter('object_exists')
        waiter.wait(Bucket=source_bucket, Key=object_key)
        s3.copy_object(Bucket=target_bucket, Key=object_key, CopySource=copy_source)
        return response['ContentType']
    except Exception as err:
        print("Error -" + str(err))
        return err
