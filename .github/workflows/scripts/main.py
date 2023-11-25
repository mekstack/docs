import os
import boto3
import re
from github import Github

aws_access_key_id = os.environ.get("STORAGE_ACCESS_KEY_ID")
aws_secret_access_key = os.environ.get("STORAGE_SECRET_ACCESS_KEY")
region = os.environ.get("STORAGE_REGION")
endpoint = os.environ.get("STORAGE_ENDPOINT")
bucket_name = os.environ.get("STORAGE_BUCKET")
github_token = os.environ.get("GITHUB_TOKEN")
github_repo = os.environ.get("GITHUB_REPO")

s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region,
    endpoint_url=endpoint,
)


def get_root_folders_in_bucket_nums(bucket):
    objects = s3.list_objects(Bucket=bucket)
    nums = []
    
    for obj in objects.get("Contents", []):
        key = obj["Key"]
        components = key.split("/")
        
        if len(components) > 0:
            folder_name = components[0]
            match = re.match(r'pr-(\d+)', folder_name)
            
            if match:
                nums.append(match.group(1))
    return nums


def get_open_pull_request_nums(github_token):
    g = Github(github_token)
    repo = g.get_repo(github_repo)
    open_pulls = repo.get_pulls(state='open')
    return [str(pull_request.number) for pull_request in open_pulls]


def delete_folder_in_bucket(bucket, folder):
    objects = s3.list_objects(Bucket=bucket, Prefix=folder)
    
    for obj in objects.get("Contents", []):
        s3.delete_object(Bucket=bucket, Key=obj["Key"])
    
    s3.delete_object(Bucket=bucket, Key=folder)


def delete_unusable_folders(bucket, git_token):
    folder_nums = get_root_folders_in_bucket_nums(bucket)
    pull_requests_nums = get_open_pull_request_nums(git_token)

    if folder_nums:
        for num in folder_nums:
            if num not in pull_requests_nums:
                folder_name = "pr-" + str(num)
                delete_folder_in_bucket(bucket, folder_name)


if __name__ == "__main__":
    delete_unusable_folders(bucket_name, github_token)
