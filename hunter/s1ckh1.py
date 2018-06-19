#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      sharmi
#
# Created:     19-06-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
n=int(raw_input())
l=[int(x) for x in raw_input().split()]
print l
for x in range(len(l)-1,0,-1):
    for i in range(x):
        if l[i]>l[i+1] :
            temp =l[i]
            l[i]=l[i+1]
            l[i+1]=temp
l1=[]
for i in range(len(l)-1,-1,-1):
    l1.append(l[i])
print ''.join(str(i) for i in l1)
