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
r=[str(x) for x in raw_input().split()]
a=r[0]
b=r[1]
l=list(a)
l1=list(b)
count=0
n=int(r[2])
for i in range(len(l)) :
    if l[i]!=l1[i]:
        count+=1
if count==n:
    print "yes"
else :
    print "no"