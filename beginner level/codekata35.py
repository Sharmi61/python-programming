#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sharmi
#
# Created:     15-07-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
s=raw_input()
try:
    if int(s):
        print "yes"
    elif float(s):
        print "yes"
except ValueError:
    print "no"