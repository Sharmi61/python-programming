#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     22-05-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a,b=raw_input().split()
a=int(a)
b=int(b)
l1=[]
l=[int(x) for x in range(a+1,b)]
for i in range(len(l)) :
    if l[i]%2==0:
        print l[i],