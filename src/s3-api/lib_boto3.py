import boto3
import botocore


def main():
    access_key = '1N8I3SDW0MIDUR0Z5MP8'
    secret_key = 'ecBlpo1SyN72KSo4I7jrj0KvXLEOsTNQzOoWATKS'
    s3_host = 'http://192.168.20.52:7480'

    bucket_name = 's3cloud'
    object_key = 'hello.txt'

    s3client = boto3.client('s3',
        aws_secret_access_key = secret_key,
        aws_access_key_id = access_key,
        endpoint_url = s3_host)

    # Get target bucket
    #print(s3client.list_buckets())
    #object = s3client.get_object(Bucket='s3cloud', Key='bootstrap-4.0.0.zip')
    
    # List bucket

    #print(s3client.bucket('s3cloud'))
    #response = s3client.list_buckets()
    #for bucket in response['Buckets']:
    #    print("Listing owned buckets returns => {0} was created on {1}\n".format(bucket['Name'], bucket['CreationDate']))

    #my_bucket = s3client.Bucket('s3cloud')
    
    # List all object
    response = s3client.list_objects(
        Bucket='s3cloud',
    )
    print(response)
    
    # get url object
    url = s3client.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': 's3cloud',
            'Key': 'bootstrap-4.0.0.zip'
        }
    )
    print(url)


if __name__ == '__main__':
    main() 