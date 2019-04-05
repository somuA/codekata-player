#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      somu
#
# Created:     05-02-2019
# Copyright:   (c) somu 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------




a,b,c,d=[],[],[],[]
a=list(input().split())
b=list(input().split())
c=list(input().split())
d=list(input().split())
if(a[1]==b[0]):
    if(b[1]==c[0]):
        if(c[1]==d[0]):
            if(d[1]==a[0]):
                print("yes")
            else:
                print("no")
        else:
            print("no")
    else:
        print("no")
else:
    print("no")










