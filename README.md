# AWS Workshop

There are 2 parts for this workshop. Part 1 is introduction and basic setup. [Part 2](https://github.com/sdadia/automating_e_commerce) is creating a real time streaming platform.

## Prerequisites

* We expect you have an AWS account. If not,  you can sign up for the first time and for the first 12 months most services are free. Sign up on [AWS](https://portal.aws.amazon.com/billing/signup#/start), you will need credit card information.

* We expect the you to be working with **Linux or Mac**.

* Experience working with Python, pip, jupyter notebook, PgAdmin. Install pgadmin for [Ubuntu](https://tecadmin.net/install-pgadmin4-on-ubuntu/) and [Mac](https://www.postgresql.org/ftp/pgadmin/pgadmin4/v4.8/macos/)

## Part 1 : AWS Basics

In this workshop we will look at setting up the following technologies in chronological order,

* AWS IAM user and AWS configure command line utility
* S3 buckets
* RDS - postgres
* Kinesis Data Stream
* Kinesis Firehose
* AWS Lambda Functions
* EC2 and security group for SuperSet


### AWS IAM User

IAM user are like ID card equivalent of real world. They just show who you are and what you can do (**Permissions**). We will create a user with name *first_time_aws_user* with **ADMIN Privilages**.

#### Procedure create IAM user

Go to top right corner click on your name, then select my security credentials.
![iam-1](./images/iam/iam-1.png)

Select Get started with IAM users.
![iam-2](./images/iam/iam-2.png)

On top left, select the Add User button in blue.
![iam-3](./images/iam/iam-3.png)

Give a user name, and select the options as shown in the picture, click Next.
![iam-4](./images/iam/iam-4.png)

Click on create group
![iam-5](./images/iam/iam-5.png)

Give your group a name, and select the Administrator privilages, click create group.
![iam-6](./images/iam/iam-6.png)

Give your group a name, and select the Administrator privilages, click create group, click Nest
![iam-7](./images/iam/iam-7.png)

Review the information and click Create user.
![iam-8](./images/iam/iam-8.png)

Click on the download .csv buttom and we save the file to secure location.
![iam-9](./images/iam/iam-9.png)

Now Log out of the account from the top right corner by selecting it under your name. Open the credentials file and check the contents. At the end you will be give the login link page, use this link for future use cases.

### AWS Configure Command Line Utility

At times we will eexcute some commands from terminal, without using the webiste console. In order to do that, we need set up the credentials so the commands can login on our behalf.

#### Procedure to configure command line

Open up terminal and install the **awscli** and **boto3** library, verify the installation using the --version command.
```
pip install awscli boto3 --user
aws --version
```
Now we can configure the credentials using the following command
```
aws configure
```
Enter the access key and secret key from the credentails file we downloaded in previous section.
Write the region as *eu-west-1* and output format as *json*
![configure-1](./images/configure/configure-1.png)


### S3 Buckets

![S3 Buckets](https://i1.wp.com/s3.amazonaws.com/aodba-cdn-bkt/wp-content/uploads/2018/03/26115940/aws-s3-bucket.png?fit=221%2C228) 

They are storage options, like google drive where you can put anything you want.

#### Procedure to create a bucket (Console)
In the find service search S3 select the first option
![s3-1](./images/s3/s3-1.png)

Click on Create Bucket on top left, give your bucket a name, make it unique, and select the region as EU (Ireland), click create
![s3-2](./images/s3/s3-2.png)

Click on the bucket, select blue upload buttom on the top left, drag and drop the files you want.
![s3-3](./images/s3/s3-3.png)


### Postgres RDS

RDS is a service for managed (maintained-backup, storage, update etc) databases -  Oracle, Postgres, Mysql, Microsoft Sql Server, Aurora.

#### Procedure to create Postgres RDS (Console)
Go to home page and search for RDS, select the first option, you should land on this page, Select the create database
![rds-1](./images/rds/rds-1.png)


Select Postgres and at the bottom check the *Only eligible for free tier*
![rds-2](./images/rds/rds-2.png)

Scroll to the bottom, in the Settings section, type your instance name, type a good username and password, click next
![rds-3](./images/rds/rds-3.png)

In the Network and Security section, select publically accessible, In the Database Options, delete anything that is box, go to the end of the page and click next.
![rds-4](./images/rds/rds-4.png)

Click on view Instances, after 5 minutes, the database will be ready
![rds-5](./images/rds/rds-5.png)

### Kinesis Data Stream and FireHose

Amazon Kinesis Data Streams (KDS) is a massively scalable and durable real-time data streaming service. KDS can continuously capture gigabytes of data per second from hundreds of thousands of sources such as website clickstreams, database event streams, financial transactions, social media feeds, IT logs, and location-tracking events.

![kinesis-0](https://d1.awsstatic.com/Products/product-name/diagrams/product-page-diagram_Amazon-Kinesis-Data-Streams.074de94302fd60948e1ad070e425eeda73d350e7.png)


#### How to create Kinesis Stream (Console)
In the find service search Kinesis and select the first option
![kinesis-1](./images/kinesis/kinesis-1.png)

Select blue button called get started on center of the page
![kinesis-2](./images/kinesis/kinesis-2.png)

Click on create data stream
![kinesis-3](./images/kinesis/kinesis-3.png)

Give your stream a name, select the number of shards as 1, click on create stream. 
![kinesis-4](./images/kinesis/kinesis-4.png)

In 30 seconds you will have created a stream.
![kinesis-5](./images/kinesis/kinesis-5.png)


#### How to connect this stream to S3 bucket using Firehoses?

In the find service search Kinesis again, Click on create delivery stream
![firehose-1](./images/firehose/firehose-1.png)

Give your stream a name, select source as kinesis stream, select the stream we just created from the drop down option, click next
![firehose-2](./images/firehose/firehose-2.png)

Leave everything as default option, click next
![firehose-3](./images/firehose/firehose-3.png)

In the Select destination click on S3, and choose the s3 buckt we created in the drop down menu, click next.
![firehose-4](./images/firehose/firehose-4.png)

Type buffer interval as 60, at bottom, choose create new IAM role, it will open a new window
![firehose-5](./images/firehose/firehose-5.png)
![firehose-6](./images/firehose/firehose-6.png)

Leave everything defualy and click allow
![firehose-7](./images/firehose/firehose-7.png)

Review the details and click on create stream, After 1 minute the delivery stream will be ready
![firehose-8](./images/firehose/firehose-8.png)
![firehose-9](./images/firehose/firehose-9.png)


#### Let's send some data to the kinesis stream

Create a new file/jupyter notebook and past the code, also change the **StreamName** value to your streamName in the last line. After one minute check the S3 bucket for a newley created file.

```python
# Save this File as : sample_producer.py
import boto3
import json

kinesis_client = boto3.clinet("kinesis", region='eu-west-1')

data = {'store_id': 13
        'transaction_id': 1234,
        'sale': 15,
        'item': ["apples", "plums", "grapes", "oranges", "beans"]
       }

# send the record
kinesis_client.put_record('Data':json.dumps(data) + "\n", # convert to json before sending the data
                          'PartitionKey': data['city'], 
                          StreamName='my-first-stream')   # change me
```


### AWS Lambda Function

AWS Lambda is a compute service that lets you run code without provisioning or managing servers. AWS Lambda executes your code only when needed and scales automatically, from a few requests per day to thousands per second. You pay only for the compute time you consume - there is no charge when your code is not running.

![lambda-0](https://d1.awsstatic.com/product-marketing/Lambda/Diagrams/product-page-diagram_Lambda-HowItWorks.68a0bcacfcf46fccf04b97f16b686ea44494303f.png)

#### Procedure to create a Lambda Function (Console)

Come to home page and search for lambda in the service section. Click on create function button.
![lambda-1](./images/lambda/lambda-1.png)

Give your functiona name, select the runtime as python, Create a role from the IAM console, select create function
![lambda-2](./images/lambda/lambda-2.png)

On the left side add the S3 trigger from the list
![lambda-4](./images/lambda/lambda-4.png)

Scroll down and select the bucket from where we will take the files, in the event type select PUT, click ADD at the bottom
![lambda-5](./images/lambda/lambda-5.png)

Scroll top and click the save buttom on the top right corner.
![lambda-6](./images/lambda/lambda-6.png)

Now we have created the lambda function, and we can start writing the code. Select the function name near the layer, scroll bottom. In this screen you can write your code.
![lambda-7](./images/lambda/lambda-7.png)

### AWS EC2 and Security groups

Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides secure, resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers. Amazon EC2’s simple web service interface allows you to obtain and configure capacity with minimal friction.

#### Launch a EC2 machine

Come to homepage and search for EC2, click in launch Instance
![ec2-1](./images/ec2/ec2-1.png)

Select ubuntu 18.04 from the list, click on select
![ec2-2](./images/ec2/ec2-2.png)

Select t2-micro from the list and click on review and launch
![ec2-3](./images/ec2/ec2-3.png)

Review the details and click on launch
![ec2-4](./images/ec2/ec2-4.png)

This will prompt to download a keypair, choose, create a new key pair, and give you kep pair a name and click on download key pair, then click on launch instance. After 1 minute you have a EC2 machine on the cloud.
![ec2-5](./images/ec2/ec2-5.png)
![ec2-6](./images/ec2/ec2-6.png)

### Setup Security Group

If you have worked in a company, you need to open specific ports for connection. Security groups tells which ports are open and for which IP addrees. We will run superset on port 8080, so we need to open that port. Currently only port 22 is open, which we need for SSHing into the remote computer. Click on the EC2 machine, in the description section, click on inbound rules. This will show the ports which are open.
![sg-1](./images/sg/sg-1.png)

Besides this, click on launch-wizard-xx, so we can configure the security settings, on the bottom of the page, go to the Inbound Tab. Here we can see only SSH is enabled, so we will edit this and add port 8080.
![sg-2](./images/sg/sg-2.png)

Click on ADD rule, select custom TCP, in the port put 8080, select source as anywhere, as we want to access the superset website from anywhere. Put descritin as shown. Click Save
![sg-3](./images/sg/sg-3.png)
![sg-4](./images/sg/sg-4.png)

#### Install superset

Lets install superset on the machine

```bash
# dependencies
sudo apt update &&  sudo apt-get install -y build-essential libssl-dev libffi-dev python3-dev python3-pip libsasl2-dev libldap2-dev
sudo pip3 install pandas==0.23.4 SQLAlchemy==1.2.2 psycopg2-binary pymssql superset

# one time setup
export FLASK_APP=superset
flask fab create-admin  --username admin123 --password admin1234 --firstname admin --lastname admin --email admin@gma.com
superset db upgrade 
superset init

# start superset
superset runserver -p 8080
```

Find public IP of your machine and go to this website

public-IP:8080
    
Login ID : admin123
    
Password : admin1234

Public IP from the description
![ec2-7](./images/ec2/ec2-7.png)
![ec2-8](./images/ec2/ec2-8.png)
