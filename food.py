n,q=input().split()
n,q=[int(n),int(q)]
a=input()
d=0
f=0
pos=list()
for i in range(n):
    if a[i]=='-':
        continue
    elif a[i]=='F':
        f+=1
        pos.append(int(i))
    elif a[i]=='D':
        pass
        #d+=1
l=len(pos)
dist=max(pos)-min(pos)-1
if l>2:
	dist-=(l-2)
#print(dist)
p=min(pos)
r=max(pos)
for i in range(p,r+1):
	if a[i]=='D':
		d+=1
while q>0:
    q-=1
    cost=0
    x, y = input().split()
    x,y=[int(x),int(y)]
    cost+=d*y
    cost+=dist*x
    print(cost)
