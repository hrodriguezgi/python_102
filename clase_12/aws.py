import os

from custom_boto3 import MyS3

# first at all: we need AWS credentials to work with boto3
aws_access_key_id = os.getenv('aws_access_key_id')
aws_secret_access_key = os.getenv('aws_secret_access_key')
aws_region = 'us-west-2'


def main():
    s3_obj = MyS3(aws_access_key_id, aws_secret_access_key, aws_region)

    #print('listando objetos de un bucket con client')
    list_bucket = s3_obj.client_list_objects('kubicall')
    for file in list_bucket:
        print(file.get('Key'))
    print()

    """print('listando objetos de un bucket con resource')
    list_bucket = s3_obj.client_list_objects('kubicall')
    print(list_bucket)"""


if __name__ == '__main__':
    main()