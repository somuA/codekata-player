a=[]
a=list(input())
s=[]
for i in range(0,len(a)):
    s.append(a[i])
s.reverse()
if(a==s):
    print('YES')
else:
    print('NO')

