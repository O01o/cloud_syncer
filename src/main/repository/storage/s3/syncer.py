import os
import subprocess
import boto3

from src.main.logic import tree

_s3_client = boto3.client('s3')
_bucket_name: str | None = None

def init_bucket(bucket_name: str):
    global _bucket_name
    _bucket_name = bucket_name

def push(local_path: str, sync_path: str, archive_mode: bool, encryption: bool):
    assert _bucket_name is not None, "bucket_name must be initialized"
    s3_path = f"s3://{_bucket_name}/{sync_path}/"
    storage_class = "DEEP_ARCHIVE" if archive_mode else "STANDARD_IA"
    s3_sync_command = [
        "aws", "s3", "sync", 
        local_path, s3_path, 
        "--storage-class", storage_class,
        "--delete"
    ]
    subprocess.run(s3_sync_command, check=True)

def push_tree(local_path: str, sync_path: str):
    assert _bucket_name is not None, "bucket_name must be initialized"
    tree_content = tree.get_tree(local_path)
    print("tree:", tree_content)
    try:
        _s3_client.put_object(
            Body=tree_content,
            Bucket=_bucket_name,
            Key=os.path.join(sync_path, "tree.txt"),
            StorageClass='STANDARD_IA',
        )
    except Exception as e:
        print(f"Error S3 uploading {local_path} to {sync_path}:", e)

def pull(local_path: str, sync_path: str):
    assert _bucket_name is not None, "bucket_name must be initialized"
    s3_path = f"s3://{_bucket_name}/{sync_path}/"
    s3_sync_command = [
        "aws", "s3", "sync", 
        s3_path, local_path, 
        "--delete"
    ]
    subprocess.run(s3_sync_command, check=True)

