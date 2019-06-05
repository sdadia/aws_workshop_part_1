import boto3
import json

# create client
kinesis_client = boto3.client('kinesis', region_name='eu-west-1')

# create stream
kinesis_client.create_stream(StreamName='taxi_fleet_stream',ShardCount=1)
## If stream already exists, then you will get a "ResourceInUseException"

# list stream
kinesis_client.list_streams()

# destory stream
kinesis_client.delete_stream(StreamName = 'taxi_fleet_stream')

# send data to stream
data = {'store_id': 13
        'transaction_id': 1234,
        'sale': 15,
        'item': ["apples", "plums", "grapes", "oranges", "beans"]
       }
kinesis_client.put_record('Data':json.dumps(data),       # convert to json before sending the data
                          'PartitionKey': data['store_id'], 
                          StreamName='my-stream-name')   # change me