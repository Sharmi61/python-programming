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

r=str(raw_input())
l=list(r)
for i in range(len(l)):
    if l[i].isupper():
        l[i]=l[i].lower()
    elif l[i].islower() :
        l[i]=l[i].upper()
s=str(l)
print s
