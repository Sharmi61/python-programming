#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     20-02-2018
# Copyright:   (c) user 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    s=" sharmi"
    l=s.count('a')
    print l
    l=s.find('a')
    print l
    print type(l)
    l=s.replace('h','a')
    print l
    print type(l)
    l=s.upper()
    print l
    l=s.strip()
    print l



if __name__ == '__main__':
    main()
