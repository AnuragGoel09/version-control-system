import os
from pathlib import Path
import json
import bin.generate_random as generate_random

def get_repo_id(VCS_PATH):
    data={}
    curr_repo_id=1
    with open(VCS_PATH+"/jsons/flags.json","r") as f:
        data=json.load(f)
    curr_repo_id=data["repo_id"]
    repo_id=generate_random.generate(10-len(str(curr_repo_id)))
    data["repo_id"]=curr_repo_id+1

    with open(VCS_PATH+"/jsons/flags.json","w") as f:
        json.dump(data,f)
    return str(curr_repo_id)+repo_id

def init(VCS_PATH,repo_path):
    repos_file_path=VCS_PATH+"/jsons/repos.json"
    data={}
    with open(repos_file_path,"r") as f:
        try:
            data=json.load(f)
            if repo_path in data:
                print("VSC ALREADY INITIALIZED")
                return data[repo_path]["repo_id"]
            else:
                raise Exception()
        except:
            repo_ID=get_repo_id(VCS_PATH)
            data[repo_path]={
                "repo_id":repo_ID,
                "commit_id":None,
                "commit_time":None,
            }
            print("VCS INITIALIZED SUCCESSFULLY")

    with open(VCS_PATH+"/jsons/repos.json","w") as repos:
        json.dump(data,repos)
    return repo_ID

def get_repo_info(VCS_PATH,repo_path):
    repos_file_path=VCS_PATH+"/jsons/repos.json"
    data={}
    with open(repos_file_path,"r") as f:
        data=json.load(f)
    if repo_path in data:
        return data[repo_path]
    else:
        return {}