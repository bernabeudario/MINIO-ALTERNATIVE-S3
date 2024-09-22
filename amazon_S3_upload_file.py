import io
import boto3

def main():
    client = boto3.client(
        's3',
        endpoint_url='http://localhost:9000',
        aws_access_key_id='<ACCESS_KEY>',
        aws_secret_access_key='<SECRET_KEY>'
    )  

    data = 'Hello World'
    data = io.BytesIO(data.encode('utf-8'))

    client.upload_fileobj(
        data, 
        'bronze',
        'messages/test/hello_world.md'
    )

if __name__ == '__main__':
    main()
