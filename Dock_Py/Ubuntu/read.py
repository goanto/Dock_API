import os
f = open("/root/requirements-apk", "r")
#f = open("requirements-apk.txt", "r")
#print(f.read())
for i in f:
    os.system("apt-get install "+ i + "  -y")