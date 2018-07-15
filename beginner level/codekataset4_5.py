#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     15-07-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#------------------------------------------------------------------------------
l=[x for x in raw_input()]
count=0;
for x in l:
    if x.isdigit():
        count=count+1
print count