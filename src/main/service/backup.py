from src.main.repository.storage.interface.backup import Backuper

_backup: Backuper | None = None

def init_backup(backup: Backuper):
    global _backup
    _backup = backup

def push(local_path: str, upload_path: str, encryption: bool):
    assert _backup is not None, "Project must be initialized"
    _backup.push(
        local_path=local_path,
        upload_path=upload_path,
        encryption=encryption,
    )

def push_tree(local_path: str, upload_path: str):
    assert _backup is not None, "Project must be initialized"
    _backup.push_tree(
        local_path=local_path,
        upload_path=upload_path,
    )

def pull(local_path: str, upload_path: str):
    assert _backup is not None, "Project must be initialized"
    _backup.pull(
        local_path=local_path,
        upload_path=upload_path,
    )