# Save this File as : sample_producer.py
import boto3
import json

kinesis_client = boto3.client("kinesis", region='eu-west-1')

data = {'store_id': 13,
        'transaction_id': 1234,
        'sale': 15,
        'item': ["apples", "plums", "grapes", "oranges", "beans"]
       }

# send the record
kinesis_client.put_record(Data=json.dumps(data) + "\n", 
                          PartitionKey= data['city'], 
                          StreamName='workshop_stream_1')   # change me
