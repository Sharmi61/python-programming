#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     06-08-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
a,b=raw_input().split()
a=int(a)
b=int(b)
c=0
l=[int(x) for x in raw_input().split()]
for x in l:
    if b==x:
        c=1
        break
if c==1:
    print 'yes'
else:
    print 'no'