#!/usr/bin/env python3
import base64

file = open("binary","rt").read()
str_hex = base64.b64decode(file.encode('utf-8')).decode('utf-8')

hex_list = [int(i+j,16) for (i,j) in zip(str_hex[::2],str_hex[1::2])]

for i in range(0,len(hex_list)-1,2):
    hex_list[i] ,hex_list[i+1] =  hex_list[i+1] , hex_list[i]
 
data = bytes(hex_list)

wf = open("output","wb").write(data)