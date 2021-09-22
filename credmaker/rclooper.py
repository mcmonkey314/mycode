#!/usr/bin/env python3
i=0 #file counter 

with open("/home/student/mycode/credmaker/csv_users.txt") as uFile:
  for line in uFile:
    line=line.split(",")
    fileName="admin.rc"+str(i)
    outFile=open(fileName,"a")
    print("export OS_AUTH_URL=" + line[0], file=outFile)
    print("export OS_IDENTITY_API_VERSION=3", file=outFile)
    print("export OS_PROJECT_NAME=" + line[1], file=outFile)
    print("export OS_PROJECT_DOMAIN_NAME=" + line[2], file=outFile)
    print("export OS_USERNAME=" + line[3], file=outFile)
    print("export OS_USER_DOMAIN_NAME=" + line[4], file=outFile)
    print("export OS_PASSWORD=" + line[5], file=outFile)
    i += 1 
    outFile.close()

