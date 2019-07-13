#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      somu
#
# Created:     13-07-2019
# Copyright:   (c) somu 2019
# Licence:     <your licence
from itertools import combinations
num,digit=map(int,input().split())
list1=[]
while(0<num):
    temp=num%10
    list1.append(temp)
    num=num//10
list1.reverse()
x=len(list1)
y=x-digit
list2=["".join(map(str, comb)) for comb in combinations(list1, y)]
list2.sort()
print(list2[0])
