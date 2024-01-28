import boto3, json

aws_region = 'AWS_REGION'
aws_access_key_id='AWS_ACCESS_KEY',
aws_secret_access_key='AWS_SECRET_KEY'

# IAM group and S3 bucket information
iam_group_name = "Developers"
s3_bucket_name = 'frontend'

# Users to be added to the IAM group
developers_users = ['Denish', 'Khrish', 'Sam', 'Peter', 'Jim']

# Create an IAM client
iam_client = boto3.client('iam', region_name=aws_region)

# Create IAM users
for user_name in developers_users:
    try:
        response = iam_client.create_user(UserName=user_name)
        print(f"IAM user '{user_name}' created successfully.")
    except iam_client.exceptions.EntityAlreadyExistsException:
        print(f"IAM user '{user_name}' already exists.")
    except Exception as e:
        print(f"Error creating IAM user '{user_name}': {str(e)}")

# Create the IAM group
try:
    iam_client.create_group(GroupName=iam_group_name)
except iam_client.exceptions.EntityAlreadyExistsException:
    print(f"IAM group '{iam_group_name}' already exists.")

# Add users to the IAM group
for user in developers_users:
    try:
        iam_client.add_user_to_group(GroupName=iam_group_name, UserName=user)
        print(f"User '{user}' added to IAM group '{iam_group_name}'.")
    except iam_client.exceptions.NoSuchEntityException:
        print(f"IAM group '{iam_group_name}' does not exist.")

# Create an S3 client
s3_client = boto3.client('s3', region_name='us-east-2')

# Create the S3 bucket
try:
    response = s3_client.create_bucket(
        Bucket=s3_bucket_name
    )
    print(f"S3 bucket '{s3_bucket_name}' created successfully.")
except s3_client.exceptions.BucketAlreadyExists as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")


# Define the policy to grant full access to the S3 bucket
s3_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": f"arn:aws:s3:::{s3_bucket_name}/*"
        }
    ]
}

s3_policy_json = json.dumps(s3_policy)

# Attach the policy to the IAM group
iam_client.put_group_policy(GroupName=iam_group_name, PolicyName='S3AccessPolicy', PolicyDocument=s3_policy_json)
print(f"Policy attached to IAM group '{iam_group_name}' granting full access to S3 bucket '{s3_bucket_name}'.")