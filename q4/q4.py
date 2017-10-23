#!/usr/bin/env python3
from struct import *

at = open("OreNoFS_AT.bin","rb")
ar_list = [] 
for i in range(16384//2):
    bin = at.read(2)
    ar_list.append(unpack('>H',bin)[0])

at.close()

cl_list = []
for ar in ar_list:
    if 1 < ar < 65527:
        cl_list.append(ar)
cl_list = sorted(cl_list)
print(cl_list)

dt = open("OreNoFS_DT.bin","rb")
for i in range(30408704//4096-4+1):
    open("output/{}.bin".format(i+4),"wb").write(dt.read(4096))

# data = b''
# for cl in cl_list:
#     dt.seek(cl)
#     data += dt.read(4096)

# f = open("output.zip","wb").write(data)