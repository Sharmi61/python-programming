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
temp=0
for i in range(len(l)):
    for j in range(len(l)):
        if l[i]<l[j]:
            temp=l[j]
            l[j]=l[i]
            l[i]=temp
for x in l:
    print x,


