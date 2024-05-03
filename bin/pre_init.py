import os
from pathlib import Path
import json

def pre_init(VCS_PATH):
    Path(VCS_PATH+"/files").mkdir(parents=True, exist_ok=True)
    Path(VCS_PATH+"/jsons").mkdir(parents=True,exist_ok=True)
    
    try:
        with open(VCS_PATH+"/jsons/flags.json","r") as f:
            data=json.load(f)
            curr_id=data["repo_id"]
    except:
        with open(VCS_PATH+"/jsons/flags.json","w") as f:
            json.dump({"repo_id": 1 ,"commit_id" : 1, "vcs_path": VCS_PATH},f)

    try:
        with open(VCS_PATH+"/jsons/repos.json","r") as f:
            data=json.load(f)
    except:
        with open(VCS_PATH+"/jsons/repos.json","w") as f:
            json.dump({},f)

    try:
        with open(VCS_PATH+"/jsons/add_status.json","r") as f:
            data=json.load(f)
    except:
        with open(VCS_PATH+"/jsons/add_status.json","w") as f:
            json.dump({},f)

    try:
        with open(VCS_PATH+"/jsons/commit_status.json","r") as f:
            data=json.load(f)
    except:
        with open(VCS_PATH+"/jsons/commit_status.json","w") as f:
            json.dump({},f)
    
    try:
        with open(VCS_PATH+"/jsons/file_track.json","r") as f:
            data=json.load(f)
    except:
        with open(VCS_PATH+"/jsons/file_track.json","w") as f:
            json.dump({},f)


