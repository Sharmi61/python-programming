#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     20-05-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

l=[int(x) for x in raw_input().split()]
l1=[]
for i in range(len(l)-1,-1,-1):
    l1.append(l[i])
x=0
while i<len(l):
    if l[i]==l1[i] :
        x=x+1
    i=i + 1
if x==len(l):
    print 'yes'
else :
    print 'no'
