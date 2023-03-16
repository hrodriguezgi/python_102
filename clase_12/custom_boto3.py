import boto3
from botocore.exceptions import ClientError

# Clients and Resources
# Clients: Clients provide a low-level interface to AWS whose methods map close
#          to 1:1 with service APIs. All service operations are supported by
#          clients. Clients are generated from a JSON service definition file.
#          https://boto3.amazonaws.com/v1/documentation/api/latest/guide/clients.html

# Resources: Resources represent an object-oriented interface to Amazon Web
#            Services (AWS). They provide a higher-level abstraction than the
#            raw, low-level calls made by service clients
#            https://boto3.amazonaws.com/v1/documentation/api/latest/guide/resources.html

# Clients
class MyS3:
    def __init__(self, aws_id, aws_key, aws_region):
        self.aws_id = aws_id
        self.aws_key = aws_key
        self.aws_region = aws_region

        self.client = boto3.client('s3',
                                   aws_access_key_id=self.aws_id,
                                   aws_secret_access_key=self.aws_key,
                                   region_name=self.aws_region
                                  )
        
        self.resource = boto3.resource('s3',
                                       aws_access_key_id=self.aws_id,
                                       aws_secret_access_key=self.aws_key,
                                       region_name=self.aws_region
                                      )

    def client_list_objects(self, bucket, prefix=''):
        """
        Reference: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/list_objects_v2.html#
        """
        try:
            objects = self.client.list_objects_v2(Bucket=bucket, Prefix=prefix)
            if 'Contents' not in objects:
                return []
            list_objects = objects['Contents']
            while objects['IsTruncated']:
                objects = self.client.list_objects_v2(
                    Bucket=bucket, ContinuationToken=objects['NextContinuationToken'])
                list_objects.extend(objects['Contents'])
            return [item for item in list_objects if item['Key'].startswith(prefix)]
        except self.client.exceptions.NoSuchBucket:
            raise Exception('Bucket name doesnt exist')
        
    def resource_list_objects(self, bucket, prefix=''):
        """
        Reference: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/list_objects_v2.html#
        """
        try:
            objects = self.client.list_objects_v2(Bucket=bucket, Prefix=prefix)
            if 'Contents' not in objects:
                return []
            list_objects = objects['Contents']
            while objects['IsTruncated']:
                objects = self.client.list_objects_v2(
                    Bucket=bucket, ContinuationToken=objects['NextContinuationToken'])
                list_objects.extend(objects['Contents'])
            return [item for item in list_objects if item['Key'].startswith(prefix)]
        except Exception as e:
            raise Exception(str(e))