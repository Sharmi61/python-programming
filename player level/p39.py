#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     05-08-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
a,b=raw_input().split()
a=int(a)
b=int(b)
l=[]
count=0;
for i in range(b):
    l.append(i*i)
for x in l:
    if a<=x and b>=x:
        count+=1
print count

