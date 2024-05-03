import os
import json
import shutil
from pathlib import Path
import time
import bin.generate_random as generate_random
import bin.add as add
def get_tracked_files(VCS_PATH,repo_id):
    newly_added_files=[]
    tracked_files=[]
    data={}
    with open(VCS_PATH+"/jsons/file_track.json","r") as f:
        data=json.load(f)
    if repo_id in data:
        tracked_files=data[repo_id]

    with open(VCS_PATH+"/jsons/add_status.json","r") as f:
        data=json.load(f)
    if repo_id in data:
        newly_added_files=data[repo_id]
    union_list=list(set(tracked_files) | set(newly_added_files))
    if len(union_list)>len(tracked_files):
        return union_list,"MODIFIED"
    with open(VCS_PATH+"/jsons/commit_status.json","r") as f:
        data=json.load(f)
    last_commit_time=0
    if data[repo_id]["commit_time"]!=None:
        last_commit_time=data[repo_id]["commit_time"]
    for file in union_list:
        file_path=Path(file)
        if file_path.exists():
            last_modified=file_path.stat().st_mtime
            if last_modified>last_commit_time:
                return union_list,"MODIFIED"
    
    return union_list,"NOT MODIFIED"

def add_commit(VCS_PATH,commit,repo_id):
    data={}
    file_path=VCS_PATH+"/jsons/commit_status.json"
    with open(file_path,"r") as f:
        data=json.load(f)

    if repo_id not in data:
        data[repo_id]={"commit":[],
                       "commit_id":None,
                       "commit_time":None}
    
    data[repo_id]["commit"].append(commit)
    data[repo_id]["commit_id"]=commit["commit_id"]
    data[repo_id]["commit_time"]=commit["commit_time"]
    with open(file_path,"w") as f:
        json.dump(data,f)

def update_track_files(VCS_PATH,files,repo_id):
    data={}
    file_path=VCS_PATH+"/jsons/file_track.json"
    with open(file_path,"r") as f:
        data=json.load(f)
    data[repo_id]=files

    with open(file_path,"w") as f:
        json.dump(data,f)


def commit(VCS_PATH,repo_id,message):
    files,state=get_tracked_files(VCS_PATH,repo_id) 
    if state=="MODIFIED":
        data={}
        
        # get commit id
        flag_file=VCS_PATH+"/jsons/flags.json"
        with open(flag_file,"r") as f:
            data=json.load(f)
        commit_id=str(data["commit_id"])+generate_random.generate(10-len(str(data["commit_id"])))
        data["commit_id"]+=1
        with open(flag_file,"w") as f:
            json.dump(data,f)
        
        #making directory for files
        dir_path=VCS_PATH+"/files/"+commit_id
        os.mkdir(dir_path)

        commit={
            "commit_id":commit_id,
            "message":message,
            "dir_path":dir_path,
            "commit_time":time.time(),
            "file_map":{}
        }
        
        # making version of file
        for i in files:
            source=i    
            dest=dir_path
            commit["file_map"][dest+"/"+source.split("/")[-1]]=source
            shutil.copy(source,dest)

        add_commit(VCS_PATH,commit,repo_id)
        update_track_files(VCS_PATH,files,repo_id)
        add.reset(VCS_PATH=VCS_PATH,repo_id=repo_id)
        print("COMMIT_SUCCESSFUL")
    else:
        print("STAGING IS UP TO DATE")