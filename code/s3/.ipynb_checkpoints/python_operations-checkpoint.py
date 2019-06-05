import boto3

# s3 clinet
s3_client = boto3.client("s3")

# create bucket
s3_client.create_bucket(Bucket="trundle_bucket") 

# list buckets
response = s3.list_buckets()
# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
          

# remove bucket
