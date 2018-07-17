#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     16-07-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

l=[x.lower() for x in raw_input().split()]
l1=list(l[0])
l1[0]=l1[0].upper()
l2=list(l[1])
l2[0]=l2[0].upper()
print "".join(l1),"".join(l2)