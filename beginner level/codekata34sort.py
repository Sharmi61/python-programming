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

n=int(raw_input())
l=[int(x) for x in raw_input().split()]
l.sort()
for x in l:
  print l,
