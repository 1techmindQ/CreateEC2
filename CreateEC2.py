# Import necessary libraries
import boto3  # Import Boto3 library for AWS interaction

# Create an AWS session and EC2 resource
aws_gui = boto3.session.Session(profile_name="")  # Establish an AWS session using the profile
ec2_gui = aws_gui.resource(service_name="ec2", region_name="us-east-1")  # Create an EC2 resource in us-east-1 region

# Launch a new EC2 instance
instances = ec2_gui.create_instances(
    ImageId='',  # Specify the Amazon Machine Image (AMI) ID
    InstanceType="t2.micro",  # Specify the instance type
    MaxCount=1, MinCount=1,  # Set maximum and minimum number of instances to launch
    SubnetId='',  # Specify the subnet where the instance will be launched
    TagSpecifications=[  # Specify tags for the instance
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'NEW PROJECT'  # Set the name tag for the instance
                }
            ]
        }
    ]
)