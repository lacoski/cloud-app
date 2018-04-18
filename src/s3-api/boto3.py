import boto3


def main():
    access_key = 'JJDEGLZSRPEM355GJC0O'
    secret_key = 'DkECQdTNxOeORL5RpFSX9gdxwaeFSptUKoQ75DvU'
    s3_host = 'http://192.168.2.134:7480'

    bucket_name = 's3cloud'
    object_key = 'hello.txt'

    s3client = boto3.client('s3',
        aws_secret_access_key = secret_key,
        aws_access_key_id = access_key,
        endpoint_url = s3_host)

    response = s3client.list_buckets()
    for bucket in response['Buckets']:
        print("Listing owned buckets returns => {0} was created on {1}\n".format(bucket['Name'], bucket['CreationDate']))

if __name__ == '__main__':
    main() 