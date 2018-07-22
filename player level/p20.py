#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     22-07-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

s=str(raw_input())
l=list(s)
l1=[]
for x in l:
    if(ord(x)<=87):
        l1.append(chr(ord(x)+3))
    elif(ord(x)==88):
        l1.append('A')
    elif(ord(x)==89):
        l1.append('B')
    else:
        l1.append('C')
print ''.join(l1)
