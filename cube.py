a=int(input())
while a>0:
    a-=1
    b=int(input())
    l=[192,442,692,942]
    if b%4==0:
        x=(b/4)-1
    else:
        x=b//4
    y=b%4
    z=(x*1000)+l[y-1]
    print(int(z))
    #print(c