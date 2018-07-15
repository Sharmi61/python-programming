#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     15-07-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
n=int(raw_input())
l=[int(x) for x in raw_input().split()]
r=l[0]
for i in range(len(l)-1):
    if(l[i]<l[i+1]):
         r=l[i+1]

print r