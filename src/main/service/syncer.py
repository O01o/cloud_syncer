import json
from src.main.repository.storage.interface.syncer import Syncer

_syncer: Syncer | None = None

def init_syncer(syncer: Syncer):
    global _syncer
    _syncer = syncer

def push(local_path: str, sync_path: str, archive_mode: bool, encryption: bool):
    assert _syncer is not None, "Syncer must be initialized"
    _syncer.push(
        local_path=local_path,
        sync_path=sync_path,
        archive_mode=archive_mode,
        encryption=encryption,
    )

def push_tree(local_path: str, sync_path: str):
    assert _syncer is not None, "Syncer must be initialized"
    _syncer.push_tree(
        local_path=local_path,
        sync_path=sync_path,
    )

def push_from_json(json_path: str, archive_mode: bool, encryption: bool):
    assert _syncer is not None, "Syncer must be initialized"
    try:
        with open(json_path) as f:
            sync_path_dict: dict[str, str] = json.load(f)
            for local_path, sync_path in sync_path_dict.items():
                _syncer.push(
                    local_path=local_path,
                    sync_path=sync_path,
                    archive_mode=archive_mode,
                    encryption=encryption,
                )
                _syncer.push_tree(
                    local_path=local_path,
                    sync_path=sync_path,
                )
    except FileExistsError:
        print(f"File Not Found: {json_path}")

def pull(local_path: str, sync_path: str):
    assert _syncer is not None, "Syncer must be initialized"
    _syncer.pull(
        local_path=local_path,
        sync_path=sync_path,
    )