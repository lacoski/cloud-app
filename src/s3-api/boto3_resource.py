import boto3

access_key = '1N8I3SDW0MIDUR0Z5MP8'
secret_key = 'ecBlpo1SyN72KSo4I7jrj0KvXLEOsTNQzOoWATKS'
s3_host = 'http://192.168.20.52:7480'
s3 = boto3.resource('s3',aws_secret_access_key = secret_key,
        aws_access_key_id = access_key,
        endpoint_url = s3_host)
bucket = s3.Bucket('s3cloud')

print(bucket.objects.all())

for object in bucket.objects.all():
    print(object)
