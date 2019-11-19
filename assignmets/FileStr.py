import os
from os import stat
import daemon
#import pwd
path1 = 'C:/assignmets'
arr = os.listdir(path1)
print(arr)
size = stat(path1).st_size
print(size)
#owner = pwd.getpwuid(os.stat("path1").st_uid).pw_name