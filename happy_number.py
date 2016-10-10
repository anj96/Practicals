a=int(input())
b=str(a)
l=list()
x=0
c=0
while (x not in l) or (x!=1):
    c+=1
    x=0
    for i in b:
        x+=int(i)**2
        print(x)
    l.append(int(x))
print(c)