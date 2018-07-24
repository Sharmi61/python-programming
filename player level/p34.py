#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     23-07-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

s=str(raw_input())
l=list(s)
i=0
for x in l:
    if x.isalpha():
        break;
    else:
         i=i+1
if i==len(l):
    print 'yes'
else:
    print 'no'
