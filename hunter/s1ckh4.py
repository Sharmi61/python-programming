#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     08-06-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def f(l,n):
    for i in range(n):
        j=0
        while(j<n) :
            if i!=j and l[i]==l[j]:
                break
            j+=1
        if j==n :
            return l[i]
    return -1
n=int(raw_input())
l1=[]
l=[int(x) for x in raw_input().split()]
s=0
l1=[]
print f(l,n)