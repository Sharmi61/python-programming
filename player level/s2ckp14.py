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

r=str(raw_input())
l=[str(x) for x in r]
l1=[]
for i in range(len(l)-1,-1,-1):
    if l[i]!='a'  and l[i]!='e'  and l[i]!='i' and l[i]!='o' and l[i]!='u' and l[i]!='A' and l[i]!='E' and l[i]!='I' and l[i]!='O' and l[i]!='U' :
        l1.append(l[i])
s=''.join(l1)
print s

