#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     08-06-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

n=int(raw_input())
l1=[]
l=[int(x) for x in raw_input().split()]
for i in range(len(l)) :
    if i==l[i] :
        l1.append(l[i])
s=0
l1.sort()
for i in range(len(l1)):
    print l1[i],
