# create stream
aws kinesis create-stream  --stream-name 'my-stream-name' --shard-count 1 --region 'eu-west-1'

# list stream
aws kinesis list-streams --region 'eu-west-1'

# describe stream
aws kinesis describe-stream --stream-name 'my-stream-name'

# delete stream
aws kinesis delete-stream --stream-name "my-stream-name"