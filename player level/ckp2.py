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
n=int(raw_input())
f=1
i=1
if n <= 5:
    for i in range(i,n+1,1):
        f=f*i
    print f