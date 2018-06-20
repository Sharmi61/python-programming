#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     20-06-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
n=raw_input()
n=int(n)
l=[int(x) for x in raw_input().split()]
l1=l[:]
for x in range(len(l)-1,0,-1):
    for i in range(x):
        if l[i]>l[i+1] :
            temp =l[i]
            l[i]=l[i+1]
            l[i+1]=temp
for i in range (len (l) -1):
 	if l[i] == l[i+1]:
 	 print l[i],




