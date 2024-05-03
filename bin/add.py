import os
from pathlib import Path
import json


def repo_to_files(files):
    for i in files:
        if os.path.isdir(i):
            files.remove(i)
            path=Path(i)
            for file_path in path.rglob('*'):
                files.append(str(file_path))
    return list(set(files))

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
    for i in files:
        print(i)
    union_list=list(set(files) | set(add_status))

    file_path=VCS_PATH+"/jsons/add_status.json"
    data={}
    with open(file_path,"r") as f:
        data=json.load(f)
    data[repo_id]=union_list
    with open(file_path,"w") as f:
        json.dump(data,f)
    print("ADD SUCCESSFUL")

def reset(VCS_PATH,repo_id):
    file_path=VCS_PATH+"/jsons/add_status.json"
    data={}
    with open(file_path,"r") as f:
        data=json.load(f)
    if repo_id in data:
        data[repo_id]=[]
    with open(file_path,"w") as f:
        json.dump(data,f)
    print("RESET SUCCESSFUL")


    
    

