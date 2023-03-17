import os
import json

from custom_boto3 import MyS3, MyEc2, MyRds

# first at all: we need AWS credentials to work with boto3
aws_access_key_id = os.getenv('aws_access_key_id')
aws_secret_access_key = os.getenv('aws_secret_access_key')
aws_region = 'us-west-2'


def main():
    s3_obj = MyS3(aws_access_key_id, aws_secret_access_key, aws_region)

    #print('listando objetos de un bucket con client')
    list_bucket = s3_obj.client_list_objects('kubicall', 2)
    for file in list_bucket:
        print(file.get('Key'))
    print()

    bucket_policy = s3_obj.resource_bucket_policy('kubicall')
    print(bucket_policy.policy)

    print()

    ec2_obj = MyEc2(aws_access_key_id, aws_secret_access_key, aws_region)
    equipos = ec2_obj.client_describe_hosts('instance-state-name', 'running')
    print(equipos.get('Reservations')[0].get('Instances')[0].get('InstanceId'))

    print()

    rds_obj = MyRds(aws_access_key_id, aws_secret_access_key, aws_region)
    rds = rds_obj.client_describe_db_instances('db-instance-id', 'banca-production')
    print(rds)

if __name__ == '__main__':
    main()