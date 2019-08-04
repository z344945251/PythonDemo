import os

cmd_res = os.system("dir")

cmd_res = os.popen("dir").read()

print("--->",cmd_res)

while(True):
    print("aaaa")