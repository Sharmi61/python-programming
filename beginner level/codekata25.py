#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     15-07-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#------------------------------------------------------------------------------
n=int(raw_input())
l=[int(x) for x in raw_input().split()]
l.sort()
q=len(l)%2
r=len(l)/2
if q!=0:
    print l[r]
else:
   print (l[r]+l[r-1])/2