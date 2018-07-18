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
l=[]
c=0
for i in range(n):
    l.append(str(raw_input()))
for x in l:
    s=0
    f=list(x)
    if(f.count('k')==1):
        s=s+f.count('k')
    if(f.count('a')==2):
        s=s+f.count('a')
    if(f.count('b')==1):
        s=s+f.count('b')
    if(f.count('l')==1):
        s=s+f.count('l')
    if(f.count('i')==1):
        s=s+f.count('i')
    if s==6:
        c=c+1
print c