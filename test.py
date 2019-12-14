import os

directory = os.fsencode("C:\\Users\\rohan\\OneDrive\\Documents\\GitHub\\StudyBud\\music")

for file in os.listdir(directory):
     filename = os.fsdecode(file)
     print(filename)
