#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     23-05-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a,b=raw_input().split()
r1=int(a)
r2=int(b)
l1=[]
r=0
l=[int(x) for x in range(r1+1,r2)]
for i in range(len(l)):
    r=str(l[i])
    p=int(r)
    l1=map(int,r)
    s=0
    for i in range(len(l1)):
        s=s+l1[i]**3
    if p==s:
        print p,
