# create bucket
aws s3 mb s3://my-bucket-name --region eu-west-1

# list bucket
aws s3 ls

# remove bucket
aws s3 rb s3://my-bucket-name --force