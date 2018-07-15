#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     15-07-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
a,b=raw_input().split()
c,d=raw_input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
r=((a*60)+b)-((c*60)+d)
if(r<0):
    r=r*-1
print r/60,
print r%60
