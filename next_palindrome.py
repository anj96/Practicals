a=int(input())
while a>0:
    a-=1
    b=int(input())
    p=0
    x=b
    while p ==0:
        x+=1
        z=str(x)
        y=z[::-1]
        if z==y:
            p=1
    print(y)