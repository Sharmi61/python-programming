#-------------------------------------------------------------------------------
#
# Author:      sharmi
#
# Created:     17-07-2018
# Copyright:   (c) sharmi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
a,b=raw_input().split()
a=int(a)
b=int(b)
s=a
count=0
j=2
for i in range(a,b+1):
    j=2
    while(j<=s):
         if s==0 or s==1:
            break
         elif s%j==0:
            break
         j=j+1
    if j==s:
        count=count+1
    s=s+1
print count
