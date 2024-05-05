# version control system (vcs)
version control system (VCS) is a lightweight version control system written in Python, inspired by Git. It provides a basic commonds for managing your project's version history.

## Features
- **Committing**: Easily commit changes to your project with a descriptive message.
- **History/Log**: View the commit history of your project to understand how it has evolved over time.
- **Restore**: Restore changes in file to last commit
- **Checkout**: Move repo to another commmit

## Installation

version control system (vcs) can be installed as follows:
- **Clone the repository**: ```git clone https://github.com/AnuragGoel09/version-control-system.git```
- **Run Setup from local repository**: ```bash setup.sh```

## Getting Started
- **Initialization**:<br/>
To initialize a repository, navigate to your project directory and run: <br />
``` 
vcs init
```
- **Add files to stagin**:<br/>
To add your files to the staging area run:<br/>
```
vcs add <file1> <file2>
```
or to add all files 
```
vcs add .
```
- **Commiting changes**:<br/>
To commit the files that are staging run:<br/>
```
vcs commit -m <message>
```

- **History**:<br/>
To check the history of all commits of the repository run:<br/>
```
vcs log
```

- **Status**:<br/>
To check status which includes unstaged files and files that are modified:<br/>
```
vcs status
```

- **Restore file**:<br/>
To restore changes of a file to last commit run:<br/>
```
vcs restore <file1> <file2>
```

- **Checkout**:<br/>
To go to another commit run:<br/>
```
vcs checkout <commit id>
```
