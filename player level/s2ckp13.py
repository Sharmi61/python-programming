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

r=str(raw_input())
l=[int(x) for x in r]
s=0
for i in range(len(l)):
    s=s+l[i]**2
print s
