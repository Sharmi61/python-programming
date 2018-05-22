#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     22-05-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
n=int(raw_input())
s=0
if n==0 or n==1:
    print 'no'
else:
    for x in range(2,n,1) :
        if n%x==0:
            print 'no'
            s=1
            break
    if s==0 :
        print 'yes'