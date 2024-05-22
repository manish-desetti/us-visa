from us_visa.configuration.aws_connection1 import S3Client

if __name__ == "__main__":
    try:
        s3_client = S3Client()
        print("S3 Client and Resource successfully created.")

        # Test S3 operation: List buckets
        buckets = s3_client.s3_client.list_buckets()
        print("Buckets:")
        for bucket in buckets['Buckets']:
            print(f"  {bucket['Name']}")

    except Exception as e:
        print(f"An error occurred: {e}")