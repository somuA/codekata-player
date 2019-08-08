from itertools import permutations
n=input()
a=[]
a=list(permutations(n))
for i in range(0,len(a)):
    print(*a[i],sep='')
