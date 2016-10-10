a=int(input())
while a>0:
    a-=1
    b=int(input())
    x=2**b
    y=str(x)
    s=0
    for i in range(len(y)):
        s+=int(y[i])
    print(s)