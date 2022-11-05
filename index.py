import urllib
import boto3
import json

s3 = boto3.client('s3')


def lambda_handler(event, context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_object_key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    response=s3.get_object(Bucket=source_bucket,Key=object_key)
    target_bucket = 'my-student-backup-data'
    copy_source = {'Bucket': source_bucket, 'Key': object_key}

    try:
        s3.copy_object(Bucket=target_bucket, Key=object_key, CopySource=copy_source)
        return response['ContentType']
    except Exception as err:
        print("Error -" + str(err))
        return err
