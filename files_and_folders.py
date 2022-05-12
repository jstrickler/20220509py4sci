import os  #  includes os.path
from datetime import datetime

folder = 'DATA'
file_name = 'alice.txt'

file_path = os.path.join(folder, file_name)
print("file_path: {}".format(file_path))

file_size = os.path.getsize(file_path)
print("file_size: {}".format(file_size))

exists = os.path.exists(file_path)
print("exists: {}\n".format(exists))

dir_name = os.path.dirname(file_path)
print("dir_name: {}".format(dir_name))
base_name = os.path.basename(file_path)
print("base_name: {}".format(base_name))
abs_path = os.path.abspath(file_path)
print("abs_path: {}\n".format(abs_path))

raw_timestamp = os.path.getmtime(file_path)
print("raw_timestamp: {}".format(raw_timestamp))
file_timestamp = datetime.fromtimestamp(raw_timestamp)
print("file_timestamp: {}\n".format(file_timestamp))

