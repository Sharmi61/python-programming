#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     23-05-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

r=str(raw_input())
l=[x for x in r]
i=0
l1=[]
for i in range(len(l)-1,-1,-1):
    l1.append(l[i])
print ''.join(l1)
