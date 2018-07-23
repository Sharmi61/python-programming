#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      sharmi
#
# Created:     22-07-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
l1=[int(x) for x in raw_input().split()]
l2=[int(x) for x in raw_input().split()]
l3=[int(x) for x in raw_input().split()]
if(l1[0]==l2[0]==l3[0]):
    print 'yes'
elif(l1[1]==l2[1]==l3[1]):
    print 'yes'
elif(l1[0]==l1[1] and l2[0]==l2[1] and l3[0]==l3[1]):
    print 'yes'
else:
    print 'no'