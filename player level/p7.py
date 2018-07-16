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

s=str(raw_input())
l=list(s)
t=l[0]
l[0]=l[1]
l[1]=t
t=l[2]
l[2]=l[3]
l[3]=t
print "".join(l)