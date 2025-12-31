import os

from src.main.logic import tree

def push(local_path: str, sync_path: str, archive_mode: bool, encryption: bool):
    print(f"print all recursive path: {local_path} -> {sync_path}")
    for root, _, files in os.walk(local_path):
        for file_child_path in files:
            local_edge_path = os.path.join(root, file_child_path)
            print(local_edge_path, os.path.relpath(local_edge_path, local_path))

def push_tree(local_path: str, sync_path: str):
    print("print tree")
    print(tree.get_tree(local_path))

def pull(local_path: str, sync_path: str):
    pass
