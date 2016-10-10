a=int(input())
while a>0:
    a-=1
    n,x=input().split()
    n,x=[int(n),int(x)]
    g=[0]*n
    s=0
    f=0
    for i in range(n):
        g[i]=int(input())
    for i in range(n):
        s+=g[i]
        if s==x:
            f=1
            break
        for j in range(i,n):
            s+=g[j]
            if s==x:
                #print('YES')
                f=1
                break
        if f==1:
            break
    if f==0:
        #print(s)
        print('NO')
    else:
        print('YES')