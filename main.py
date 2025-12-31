import os
from dotenv import load_dotenv

from src.main.repository.storage.s3 import syncer as backup_s3_repository
from src.main.service import syncer as backup_service

load_dotenv()

local_path: str = os.path.join(".", "src")
sync_path: str = os.path.join("project", "this")

backup_s3_repository.init_bucket(bucket_name=os.getenv('BACKUP_BUCKET_NAME'))
backup_service.init_syncer(backup=backup_s3_repository)
backup_service.push_from_json(
    json_path='data/sync_path.json',
    archive_mode=False,
    encryption=False,
)
backup_service.push_from_json(
    json_path='data/sync_path_archive.json',
    archive_mode=True,
    encryption=False,
)