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

r=raw_input()
p=int(r)
l=map(int,r)
s=0
for i in range(len(l)):
    s=s+l[i]**3
if p==s:
    print 'yes'
else:
    print 'no'