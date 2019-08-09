a,b=input().split()
li=list(b)
c=0
for i in range(0,len(li)):
    if a[i]!=b[i]:
        c=+1
if c==1:
    print('yes')
else:
    print('no')
