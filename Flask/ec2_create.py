import boto3

ec2 = boto3.client('ec2')

image_id = 'ami-0057a15b87f6559cf'
instance_type = 't2.micro'
key_name = 'latestkeypair'
security_group_ids = ['sg-0e4c8273e546ble234']
subnet_id = 'subnet-b40f67e63'

response = ec2.run_instances(ImageId = image_id, InstanceType=instance_type, KeyName = key_name)

instance_id = response['Instances'][0]['InstanceId']

