import sys
import os

startPath = sys.argv[1]
print("Directory Path: " + startPath)
print("Directory Name: " + os.path.dirname(startPath))