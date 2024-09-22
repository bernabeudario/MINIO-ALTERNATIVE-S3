import io
from minio import Minio

def main():
    client = Minio(
        endpoint='localhost:9000',
        access_key='<ACCESS_KEY>',
        secret_key='<SECRET_KEY>',
        secure=False
    )

    data = 'Hello World'
    data = io.BytesIO(data.encode('utf-8'))

    client.put_object(
        'bronze',
        'messages/test/hello_world.md',
        data,
        length=len(data.getbuffer())
    )

if __name__ == '__main__':
    main()
