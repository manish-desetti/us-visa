import boto3
import os
from us_visa.constants import AWS_SECRET_ACCESS_KEY_ENV_KEY, AWS_ACCESS_KEY_ID_ENV_KEY, REGION_NAME
from dotenv import load_dotenv

class S3Client:
    s3_client = None
    s3_resource = None

    def __init__(self, region_name=REGION_NAME):
        """ 
        This class initializes an S3 client and resource using AWS credentials from environment variables.
        Raises an exception if the required environment variables are not set.
        """
        load_dotenv()  # Load environment variables from a .env file if present

        if S3Client.s3_client is None or S3Client.s3_resource is None:
            access_key_id = os.getenv(AWS_ACCESS_KEY_ID_ENV_KEY)
            secret_access_key = os.getenv(AWS_SECRET_ACCESS_KEY_ENV_KEY)

            print(f"Access Key ID: {access_key_id}")
            print(f"Secret Access Key: {secret_access_key}")

            if access_key_id is None:
                raise Exception(f"Environment variable '{AWS_ACCESS_KEY_ID_ENV_KEY}' is not set.")
            if secret_access_key is None:
                raise Exception(f"Environment variable '{AWS_SECRET_ACCESS_KEY_ENV_KEY}' is not set.")

            # Initialize S3 resource
            S3Client.s3_resource = boto3.resource(
                's3',
                aws_access_key_id=access_key_id,
                aws_secret_access_key=secret_access_key,
                region_name=region_name
            )

            # Initialize S3 client
            S3Client.s3_client = boto3.client(
                's3',
                aws_access_key_id=access_key_id,
                aws_secret_access_key=secret_access_key,
                region_name=region_name
            )

        # Assign the class-level clients to the instance
        self.s3_resource = S3Client.s3_resource
        self.s3_client = S3Client.s3_client
