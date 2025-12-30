import os
from dotenv import load_dotenv

from src.main.repository.storage.s3 import backup as backup_s3_repository
from src.main.repository.storage.mock import backup as backup_mock_repository

from src.main.service import backup as backup_service

load_dotenv()

local_path: str = os.path.join(".", "src")
upload_path: str = os.path.join("project", "this")

backup_s3_repository.init_bucket(bucket_name=os.getenv('BACKUP_BUCKET_NAME'))
backup_service.init_backup(backup=backup_s3_repository)
# backup_service.init_backup(backup=backup_mock_repository)
backup_service.push(
    local_path=local_path,
    upload_path=upload_path,
    encryption=False,
)
backup_service.push_tree(
    local_path=local_path,
    upload_path=upload_path,
)
