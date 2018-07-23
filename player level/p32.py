#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      sharmi
#
# Created:     23-07-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def gcd(a,b):
    if a==0 and b==0:
        return 0
    if a==b:
        return a
    if(a>b):
        return gcd(a-b,b)
    return gcd(a,b-a)

a,b=raw_input().split()
a=int(a)
b=int(b)
print gcd(a,b)
