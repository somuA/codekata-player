#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      somu
#
# Created:     13-07-2019
# Copyright:   (c) somu 2019
# Licence:     <your licence
n = int(input())
list1 = []
count=0
for i in range(0,n):
    s = input()
    list1.append(s)
list1.sort()
start=list1[0]
end=list1[n-1]
for i in range(0,10000):
    if(start[0:i]==end[0:i]):
        count=count+1
    else:
        break
print(start[0:count-1])

