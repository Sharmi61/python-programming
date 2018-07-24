#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     24-07-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
s=raw_input()
l=[str(x) for x in raw_input().split()]
l.sort()
for i in range(len(l)):
    for j in range(len(l)):
        if len(l[i])>len(l[j]):
            l.append(l[i])
            l.remove(l[i])
for x in l:
    print x,
