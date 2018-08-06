#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     06-08-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

x=raw_input();
l=list(x)
bo=0
bc=0
for i in l:
    if i=="(":
        bo+=1
    else:
        bc+=1
if bo==bc:
    print 'yes'
else:
    print 'no'
