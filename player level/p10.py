#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     17-07-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a,b=raw_input().split()
a=str(a)
b=str(b)
l1=list(a)
l2=list(b)
count=0
for i in range(len(l1)):
    if l1[i]!=l2[i]:
        count=count+1
if(count==1):
    print "yes"
else:
    print "no"
