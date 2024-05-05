import os
import json
from pathlib import Path

def get_tracked_files(VCS_PATH,repo_id):
    file_path=VCS_PATH+"/jsons/file_track.json"
    data={}
    with open(file_path,"r") as f:
        data=json.load(f)
    if repo_id in data:
        return data[repo_id]
    return []

def get_added_files(VCS_PATH,repo_id):
    file_path=VCS_PATH+"/jsons/add_status.json"
    data={}
    with open(file_path,"r") as f:
        data=json.load(f)
    if repo_id in data:
        return data[repo_id]
    return []
    
def get_all_repo_files(VCS_PATH,repo_id):
    file_path=VCS_PATH+"/jsons/repos.json"
    data={}
    with open(file_path,"r") as f:
        data=json.load(f)
    repo_path=""
    for i in data:
        if data[i]==repo_id:
            repo_path=i
    files=[]
    path=Path(repo_path)
    for file_path in path.rglob('*'):
        files.append(str(file_path))
    files_with_absolute_path=[]
    for i in files:
        files_with_absolute_path.append(os.path.abspath(i))
    return files_with_absolute_path
    
def get_status(VCS_PATH,repo_id):
    track_files=get_tracked_files(VCS_PATH,repo_id)
    add_files=get_added_files(VCS_PATH,repo_id)
    all_files=list(set(track_files)| set(add_files))
    repo_files=get_all_repo_files(VCS_PATH,repo_id)
    unstaged_files=[]
    for i in repo_files:
        if i not in all_files:
            unstaged_files.append(i)
    last_commit_time=0
    data={}
    with open(VCS_PATH+"/jsons/commit_status.json","r") as f:
        data=json.load(f)
    if repo_id in data:
        last_commit_time=data[repo_id]["commit_time"]
    if last_commit_time==None:
        last_commit_time=0
    for file in all_files:
        last_modified=Path(file).stat().st_mtime
        if(last_modified>last_commit_time):
            print(f"modified : {file}")    
    print("")
    for file in unstaged_files:
        print(f"unstaged : {file}")
    

def get_commits(VCS_PATH,repo_id):
    file_path=VCS_PATH+"/jsons/commit_status.json"
    data={}
    with open(file_path,"r") as f:
        data=json.load(f)
    if repo_id not in data:
        return {},None
    return data[repo_id]["commit"],data[repo_id]["commit_id"]

def get_log(VCS_PATH,repo_id):
    all_commits,curr_commit=get_commits(VCS_PATH,repo_id)
    if curr_commit==None:
        print("No previous record")
        exit(0)
    print(f"current commit id - {curr_commit}")
    print("--------------------------")      
    for i in all_commits:
        print(f"commit id - {all_commits[i]['commit_id']}")
        print(f"message - {all_commits[i]['message']}")
        print("--------------------------")  