s=raw_input()

l=['a','e','i','o','u']

r=1

for x in l:
	
             if s == x:
		
             r=0
		
            break

if r==0:
	
  print "vowel"

elif r!=0 :
	
 print "constant"