from bin import pre_init
from bin import init , add
import sys
VCS_PATH="/mnt/d/Projects/version-control-system"


def handle_init(repo_path):
    repo_ID=init.init(VCS_PATH=VCS_PATH,repo_path=repo_path)
    print(f"REPOSITORY ID : {repo_ID}")

def handle_add(repo_path,args):
    for i in args:
        if i==".":
            args.remove(i)
            args.append(repo_path)
    repo_info=init.get_repo_info(VCS_PATH=VCS_PATH,repo_path=repo_path)
    if "repo_id" in repo_info:
        add.add_files(VCS_PATH=VCS_PATH,repo_id=repo_info["repo_id"],files=args)
    else:
        print("VCS NOT INITIALIZED")

def handle_reset(repo_path):
    repo_info=init.get_repo_info(VCS_PATH=VCS_PATH,repo_path=repo_path)
    if "repo_id" in repo_info:
        add.reset(VCS_PATH=VCS_PATH,repo_id=repo_info["repo_id"])
    else:
        print("VCS NOT INITIALIZED")

if __name__=="__main__":
    repo_path=sys.argv[1].rstrip("\r")
    args=sys.argv[2:]    
    pre_init.pre_init(VCS_PATH=VCS_PATH)
    try:
        if len(args)==0:
            raise Exception()
        elif args[0]=="init" and len(args)==1:
            handle_init(repo_path)
        elif args[0]=="add" and len(args)>1:
            handle_add(repo_path,args[1:])
        elif args[0]=="reset" and len(args)==1:
            handle_reset(repo_path)
        else:
            raise Exception()

    except:
        print("Invalid Arguments")
        exit(0)
