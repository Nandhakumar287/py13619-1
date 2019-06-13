n=int(input())
li=list(map(int,input().split()))[:n]
l=list()
rev=-1
forward=0
li.sort()
for i in range(0,n):
    if(i%2==0):
        l.append(li[rev])
        rev-=1
    else:
        l.append(li[forward])
        forward+=1
print(l)     
