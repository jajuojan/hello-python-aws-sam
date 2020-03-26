import os
import json
import requests
import boto3
import io

def lambda_handler(event, context):
    # Print message to CW log
    print("Hello World!")

    # Get env-variables
    download_url = os.environ['DOWNLOADURL']
    bucket_name = os.environ['BUCKETNAME']
    key_name = os.environ['KEYNAME']

    # Grab file
    content = requests.get(download_url)
    cnt = io.BytesIO(content.content)

    # Send to S3 bucket
    s3 = boto3.client('s3')
    s3.upload_fileobj(cnt, bucket_name, key_name)

     # Happy case
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'hello world',
            'size': len(content.content)
        }),
    }
