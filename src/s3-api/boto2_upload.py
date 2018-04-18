import os
import boto
import boto.s3.connection
from boto.s3.key import Key

def upload_to_s3(file, bucket, key, callback=None, md5=None, reduced_redundancy=False, content_type=None):

    try:
        size = os.fstat(file.fileno()).st_size
    except:
        # Not all file objects implement fileno(),
        # so we fall back on this
        file.seek(0, os.SEEK_END)
        size = file.tell()

    access_key = 'JJDEGLZSRPEM355GJC0O'
    secret_key = 'DkECQdTNxOeORL5RpFSX9gdxwaeFSptUKoQ75DvU'
    conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        host = '192.168.2.134', 
        port = 7480,
        is_secure=False, 
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
    )
    bucket = conn.get_bucket(bucket, validate=True)
    k = Key(bucket)
    k.key = key
    if content_type:
        k.set_metadata('Content-Type', content_type)
    sent = k.set_contents_from_file(file, cb=callback, md5=md5, reduced_redundancy=reduced_redundancy, rewind=True)

    # Rewind for later use
    file.seek(0)

    if sent == size:
        return True
    return False

def main():
    file = open('/home/lacoski/Downloads/highlight.zip', 'r+')

    key = file.name
    bucket = 's3cloud'

    if upload_to_s3(file, bucket, key):
        print('It worked!')
    else:
        print('The upload failed...')

if __name__ == "__main__":
    main()