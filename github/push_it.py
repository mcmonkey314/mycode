#!/usr/bin/env python3
import os 
commit_msg = input('Commit Comment:')
working_dir = 'cd ~/mycode/'
git_add = 'git add *'
git_commit = 'git commit -m "'+commit_msg+'"'
git_push = 'git push origin'

os.system(working_dir)
os.system(git_add)
os.system(git_commit)
os.system(git_push)

