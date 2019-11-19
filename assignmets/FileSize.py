import os

myPath = "C:/assignmets"

mySize = '194'

filesList= []

for path, subdirs, files in os.walk(myPath):
    for name in files:
        filesList.append(os.path.join(path, name))

for i in filesList:
    fileSize = os.path.getsize(str(i))
    if int(fileSize) >= int(mySize):
        print("The File: " + str(i) + " is: " + str(fileSize) + " Bytes")