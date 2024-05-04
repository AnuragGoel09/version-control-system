import os
from pathlib import Path
import json
import sys

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

def get_add_status(VCS_PATH,repo_id):
    data={}
    with open(VCS_PATH+"/jsons/add_status.json","r") as f:
        data=json.load(f)
    if repo_id in data:
        return data[repo_id]
    return []

def add_files(VCS_PATH,repo_id,files):
    
    files=repo_to_files(files)
    add_status=get_add_status(VCS_PATH,repo_id)    
    union_list=list(set(files) | set(add_status))

    file_path=VCS_PATH+"/jsons/add_status.json"
    data={}
    with open(file_path,"r") as f:
        data=json.load(f)
    data[repo_id]=union_list
    print(union_list)
    with open(file_path,"w") as f:
        json.dump(data,f)

def reset(VCS_PATH,repo_id):
    file_path=VCS_PATH+"/jsons/add_status.json"
    data={}
    with open(file_path,"r") as f:
        data=json.load(f)
    if repo_id in data:
        data[repo_id]=[]
    with open(file_path,"w") as f:
        json.dump(data,f)
    


    
    

