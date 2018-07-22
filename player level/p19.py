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

n=int(raw_input())
i=2
j=2
l=[]
while(i<=n):
    if(n%i==0):
       j=2
       while(j<i):
        if(i%j==0):
            break
        j=j+1
       if i==j:
        l.append(i)
    i=i+1
for x in l:
    print x,