# f = open("test.txt",'w')
# f.write("Hello python")

# f = open("test.txt",'r')
# data = f.read()
# print(data)

# f = open("test.txt",'a')
# f.write("Hello python")

# f = open("test.txt",'r')
# data = f.readlines()
# print(data)
# f.close()

# f = open("test.txt",'r')
# while True:
#     data = f.readline()
#     print(data)
#     if data.strip().endswith("n"):
#         break
#     if not data:
#         break
# f.close()

# with open("test.txt",'r') as f:
#     f.seek(15)
#     print(f.tell())
#     data = f.read()
#     print(f.tell())
#     print(data)

# with open("Capture.png",'rb') as f:
#     d = f.read()
#     print(d)

# with open("home.txt",'r+') as f:
#     f.write("Python programming...")
#     f.seek(0)
#     data = f.read()
#     print(data)

import os

# os.mkdir("New Folder")
# os.rmdir("New Folder")