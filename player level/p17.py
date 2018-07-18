#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     18-07-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a,b=raw_input().split()
a=int(a)
b=int(b)
if a==b:
    print a
else:
    if a>b:
        m=a
    elif b>a:
        m=b
    while(1):
        if m%a==0 and m%b==0:
            print m
            break
        m=m+1

