#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     27-05-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a,b=raw_input().split()
a=int(a)
b=int(b)
l=[int(x) for x in raw_input().split()]
l1= l[len(l)-b:]   + l[:len(l)-b]
i=0
while i<len(l1) :
    print l1[i],
    i=i+1