import sys
import os

path = sys.argv[1]

# Check if path exits
if os.path.exists(path):
    print("Directory exist")

# Get filename
print("Directory name : " + path.split("/")[1])