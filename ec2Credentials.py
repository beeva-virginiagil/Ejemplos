import boto3
import yaml

def openSession():
    with open("/home/virginiagil/amazon/examples/config/credentials.yaml","r") as credentials_file:

        credentials=yaml.load(credentials_file)

        session=boto3.Session(aws_access_key_id=credentials['config']['aws_access'],
                              aws_secret_access_key=credentials['config']['aws_secret'])

    return session