#!/usr/bin/env python3
from struct import *
import os

ore = (2048*512, 59392*512) # (starr,length) cut gpt
cl_size = 4096
at_size = cl_size * 4 # AllocationTable
de_size = 32 # Directory entory

with open("raw.dmg","rb") as raw:
    raw.seek(ore[0])
    with open("OreNoFS.bin","wb") as f:
        f.write(raw.read(ore[1]))

with open("OreNoFS.bin","rb") as at:
    with open("at.bin","wb") as f:
        f.write(at.read(at_size))
    with open("de.bin","wb") as f:
        f.write(at.read(de_size))

with open("de.bin","rb") as de:
    de.seek(1)
    print("file_name: {}".format(de.read(8)))
    de.seek(12)
    file_size = unpack('<l',de.read(4))[0]
    print("file_size: {} byte".format(file_size))
    offset_of_cluster = unpack('<H',de.read(2))[0]
    print("offset_of_cluster: {} cluster".format(offset_of_cluster))

with open("at.bin","rb") as at:
    at_list = []
    for i in range(at_size // 2): # 2 byteごとなので
        bin = at.read(2)
        at_list.append(unpack('<H',bin)[0])

with open("OreNoFS.bin","rb") as f:
    os.mkdir("cluster")
    for i in range(ore[1] // cl_size):
        open("cluster/{}.bin".format(i),"wb").write(f.read(cl_size))

with open("result.zip","ab") as r: # 追記モード
    cluster = offset_of_cluster
    for i in range(len(at_list)):
        if 1 < cluster < 65527:
            r.write(open("cluster/{}.bin".format(cluster),"rb").read())
            cluster = at_list[cluster]
