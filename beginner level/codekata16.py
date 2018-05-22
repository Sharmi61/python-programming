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
s=0
l=[int(x) for x in range(a+1,b)]
for i in range(len(l)) :
    if l[i]!=0 and l[i]!=1 and l[i]!=2 :
        for x in range(2,l[i],1) :
            if l[i]%x==0:
                 s=1
                 break
            else :
                s=0
        if s==0 :
            print l[i],