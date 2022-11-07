import urllib
import boto3

s3 = boto3.client('s3')


def lambda_handler(event, context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_object_key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    target_bucket = 'my-student-backup-data'
    copy_source = {'Bucket': source_bucket, 'Key': source_object_key}

    try:
        s3.copy_object(Bucket=target_bucket, Key=source_object_key, CopySource=copy_source)
    except Exception as err:
        print("Error -" + str(err))
        return err
