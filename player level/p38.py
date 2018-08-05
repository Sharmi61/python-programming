#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     05-08-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------  \
r=str(raw_input())
l=list(r)
s=len(l)-1
for i in range(s):
    if l[i]==" ":
        l.remove(l[i])
        if i!=s-1:
            s=s-1
        else:
            break

s1="".join(l)
print s1
