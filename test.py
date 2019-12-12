import os

directory_in_str = os.path.join(os.getcwd(), "music")
directory = os.fsencode(directory_in_str)

for file in os.listdir(directory):
     filename = os.fsdecode(file)
     print(os.path.join(os.getcwd(), filename))
