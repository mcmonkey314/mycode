#!/usr/bin/env python3
## create file object in "r"ead mode
#lines=0
filename=input("What is the name of the file: ")
with open(filename, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    #lines += 1
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print("There were "+str(configlist.__len__())+" lines in the file.")
