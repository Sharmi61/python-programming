#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     19-05-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#------------------------------------------------------------------------------
a,b=raw_input().split()
a= int(a)
b= int(b)
l=[int(x) for x in raw_input().split()]
print l
r=0
i=0
for i in l[0:b ]:
    r=r+i
print r

