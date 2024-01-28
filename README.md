# Creating S3 Bucket and Adding User Group with Full Access using Python
This repository contains Python scripts to create an S3 bucket and add a user group with full access to the bucket programmatically.

## Prerequisites
Before running the scripts, ensure you have the following:

- Python installed on your local machine.
- AWS credentials configured with appropriate permissions to create resources and manage IAM users and groups.

### Usage
Follow these steps to create an S3 bucket and add a user group with full access using Python:

1. Clone the Repository:

```bash
git clone https://github.com/denishjackson1/cloudautomation-python.git
cd cloudautomation-python
```

2. Activate virtual environment `venv`

```bash
python3 -m venv venv
source venv/bin/activate

```
3. Install Dependencies:

```bash
pip install boto3
```
4. Run the Script in `main.py`

```bash
python3 main.py
```
## Accessing the Bucket:
Once the scripts are executed successfully, you can access the created S3 bucket through the AWS Management Console or AWS CLI.