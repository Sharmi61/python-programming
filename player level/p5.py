#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     16-07-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

r=str(raw_input())
s=list(r)
c=0
for x in s:
    if x=="I":
        c=c+1
    elif x=="V" and c==1 :
        c=4
    elif x=="V" and c==11 :
        c=14
    elif x=="V":
        c=c+5
    elif x=="X" and c==1:
        c=9
    elif x=="X" and c==11:
        c=19
    elif x=="X":
        c=c+10

print c
