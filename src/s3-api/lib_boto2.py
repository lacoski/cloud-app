import boto
import boto.s3.connection
from boto.s3.key import Key

access_key = '1N8I3SDW0MIDUR0Z5MP8'
secret_key = 'ecBlpo1SyN72KSo4I7jrj0KvXLEOsTNQzOoWATKS'
conn = boto.connect_s3(
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_key,
    host = '192.168.20.52', 
    port = 7480,
    is_secure=False, 
    calling_format = boto.s3.connection.OrdinaryCallingFormat(),
   )

def create_bucket():
    bucket = conn.create_bucket('s3cloud')

def list_bucket():
    for bucket in conn.get_all_buckets():
        print(bucket.name)

def list_bucket_content():
    for key in bucket.list():
        print(
            key.name + " " +
            key.size + " " +
            key.last_modified
        )

def access_bucket():
    bucket = conn.get_bucket('s3cloud', validate=False)
    exists = conn.lookup('s3cloud')
    for key in bucket.list():
        print(key.name)
        print("Name: {0} - size: {1} - Last modified:{2}".format(key.name, key.size, key.last_modified))

def store_data():
    bucket = conn.get_bucket('s3cloud', validate=False)
    key = bucket.new_key('hello.txt')
    key.set_contents_from_string('Hello World! aaaaa')

def download_object():
    bucket = conn.get_bucket('s3cloud', validate=False)
    key = bucket.get_key('hello.txt')
    key.get_contents_to_filename('/home/lacoski/Documents/hello.txt')
def delete_object():
    bucket = conn.get_bucket('s3cloud', validate=False)
    bucket.delete_key('hello.txt')

def generate_object_url():
    bucket = conn.get_bucket('s3cloud', validate=False)
    hello_key = bucket.get_key('hello.txt')
    hello_url = hello_key.generate_url(0, query_auth=False, force_http=True)
    print(hello_url)

def set_acl_obj():
    bucket = conn.get_bucket('s3cloud', validate=False)
    hello_key = bucket.get_key('hello.txt')
    hello_key.set_canned_acl('public-read')

def upload_and_geturl():
    bucket = conn.get_bucket('s3cloud', validate=False)
    key = bucket.new_key('hello.txt')
    key.set_contents_from_string('Hello World! aaaaa')

def main():  
    create_bucket()
    #store_data()
    #set_acl_obj()
    #generate_object_url()
    list_bucket()
    #access_bucket()
    #download_object()
    #delete_object()
    #access_bucket()

if __name__ == "__main__":
    main()