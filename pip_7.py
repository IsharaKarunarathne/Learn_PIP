import os

#list content of current dictionary

print("contents of current dictionary")

for item in os.listdir('.'):
    print(item)

#can also specify a path
#to get list contents of the /tmp directory:
#print("\ncontents of /tmp dictionary:")
#for item in os.listdir('/tmp'):
    #print(item)