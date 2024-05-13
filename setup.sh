#!/bin/bash
vcs_path=$(pwd)

vcs_content='path=$(pwd)
python3 '$vcs_path'/main.py $path '$vcs_path' $@
'
echo "$vcs_content" > vcs

chmod +x vcs
mkdir -p ~/bin
mv vcs ~/bin/
export PATH="$PATH:$HOME/bin"
source ~/.bashrc
