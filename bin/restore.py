import json
from pathlib import Path
import shutil
import os
import time

def repo_to_files(files):
    for i in files:
        if os.path.isdir(i):
            files.remove(i)
            path=Path(i)
            for file_path in path.rglob('*'):
                files.append(str(file_path))
    files_with_absolute_path=[]
    for i in files:
        files_with_absolute_path.append(os.path.abspath(i))
    return list(set(files_with_absolute_path))

def check_files_track(VCS_PATH,repo_id,files):
    file_path=VCS_PATH+"/jsons/file_track.json"
    data={}
    with open(file_path,"r") as f:
        data=json.load(f)
    if repo_id not in data:
        return False
    for i in files:
        if i not in data[repo_id]:
            return False
    return True

def copy_files(VCS_PATH,repo_id,files):
    data={}
    file_map={}
    file_path=VCS_PATH+"/jsons/commit_status.json"
    with open(file_path,"r") as f:
        data=json.load(f)[repo_id]
    curr_commit=data["commit_id"]
    file_map=data["commit"][curr_commit]["file_map"]
    for file in files:
        for i in file_map:
            if file_map[i]==file:
                os.makedirs(os.path.dirname(file), exist_ok=True)
                shutil.copy(i,file)

def restore_file(VCS_PATH,repo_id,files):
    
    files=repo_to_files(files)
    if(check_files_track(VCS_PATH=VCS_PATH,repo_id=repo_id,files=files)):
        copy_files(VCS_PATH,repo_id,files)
    else:
        print("file path does not exist")

def restore_all_files(file_map):
    for i in file_map:
        os.makedirs(os.path.dirname(file_map[i]), exist_ok=True)
        shutil.copy(i,file_map[i])

def checkout(VCS_PATH,repo_id,commit_id):
    data={}
    with open(VCS_PATH+"/jsons/commit_status.json","r")as f:
        data=json.load(f)
    if repo_id not in data or commit_id not in data[repo_id]["commit"]:
        print(f"{commit_id} does not exists")
    else:
        restore_all_files(data[repo_id]["commit"][commit_id]["file_map"])
        data[repo_id]["commit_id"]=commit_id
        data[repo_id]["commit_time"]=time.time()
    
    