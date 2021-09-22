#!/usr/bin/env python3
"""Alta3 Research | RZFeeser@alta3.com
   Using python to create compressed (zipped) archives"""

# standard library imports
import os      # low-level, operating system agnostic commands (i.e. supports most OSes)
import zipfile # tools to create, read, write, append, and list a ZIP file

# function to search for all files within a directory, and add them to our ZIP
def zipCheck(zipfileobj):
  zipfileobj=zipfileobj
  if zipfile.is_zipfile(zipfileobj):
    print ("Yep..this is a legit zip file")
  else:
    print ("Nope - this is some janky bogus file.")
  return None

def main():
  zipfileobj=input("Enter the name of the file that you would like to check: ")
  zipCheck(zipfileobj)

main()

