#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     17-07-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
n=raw_input()
l=[int(x) for x in raw_input().split()]
l1=[]
count=0
for i in range(len(l)):
    for j in range(len(l)):
        if i!=j:
            if(l[i]==l[j]):
                count=count+1
    l1.append(count)
    count=0
    j=0
i=l1.index(0)
print l[i]