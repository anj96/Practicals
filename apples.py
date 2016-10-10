i=10
while i>0:
    i-=1
    n=int(input())
    p=int(input())
    q=n//2
    r=p//2
    #print(r)
    if p%2==0:
        x=q+r
        y=q-r
    else:
        x=q+r
        y=q-r-1
    print(x)
    print(y)