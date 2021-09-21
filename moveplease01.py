#!/usr/bin/env python3

#import libraries for high-level and os commands
import shutil
import os

def main():

  #change to working directory
  os.chdir('/home/student/mycode/')
  #copy from current directory to ceph_storage
  shutil.move('raynor.obj', 'ceph_storage/')

  #prompt for new file name of kerrigan.obj
  xname = input('What is the new name for kerrigan.obj? ')

  #copy kerrigan to the same location, but with the new name
  shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

# call main routine
main()
