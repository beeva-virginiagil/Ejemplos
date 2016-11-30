#from bottle import get, route,run,post

import boto3
from examples.ec2Credentials import openSession

#client = boto3.client('ec2')
#boto = boto3.Session(profile_name='dev') En caso ded que tengamos varias keys

#print client.describe_instances()

def get_instances():
    instances=list()
    client= boto3.client('ec2')
    ec2=client.describe_instances()

    for i in ec2['Reservations']:
        for x in i['Instances']:
            for s in x['Tags']:
                if s['Key'] == "Name":
                    instances.append(s['Value'])
    return instances


def get_volumes():
    volumes=list()
    client=boto3.client('ec2')
    ec2=client.describe_volumes()

    for i in ec2['Volumes']:
        for x in i['Attachments']:
            volumes.append(x['InstanceId'])
    return volumes


def get_vpcs():
    vpcs = list()
    client = boto3.client('ec2')
    ec2 = client.describe_vpcs()

    for i in ec2['Vpcs']:
        vpcs.append(i['VpcId'])
    return vpcs

def get_instanceIdfromName():
    client=boto3.client('ec2')
    ec2= client.describe_instances(
        Filters=[
            {
                'Name':'tag-value',
                'Values':['AlphaGroup'],
            }
        ])

    for i in ec2['Reservations']:
        for x in i ['Instances']:
            instanceId=x['InstanceId']

    return instanceId



def put_tagInstance(value):
    client=boto3.resource('ec2')
    client.create_tags(Resources=[get_instanceIdfromName()],Tags=[
        {
            'Key':'Devops-Virginia',
            'Value': value
        }])

#put_tagInstance('virginia')

def launch_instance():
    client = openSession().client('ec2')
    instances= client.run_instances(ImageId='ami-9398d3e0',MinCount=1,MaxCount=1,KeyName='virginia-key',
                                    InstanceType='t2.micro',Monitoring={'Enabled':False},
                                    NetworkInterfaces=[{'DeviceIndex': 0,'AssociatePublicIpAddress':True,
                                                        'SubnetId':'subnet-f1e770a9'}])

launch_instance()




           # for s in x['BlockDeviceMappings']:
            #    for n in s['Ebs']:
               #     for m in n ["VolumeId"]:
                #        print m
            # volumes.append()

#print client.describe_volumes()
#print client.describe_vpcs()
#print client.describe_images()

# instances.append(x['InstancesId'])
