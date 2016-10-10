a=int(input())
while a>0:
    a-=1
    n,x=input().split()
    n=int(n)
    x=int(x)
    str_arr=input().split()
    arr=[int(x)for x in str_arr]
    y=sorted(arr)
    total=0
    cnt=0
    while total<x:
        if cnt<n:
            total+=y[cnt]
            cnt+=1
        else:
            cnt+=1
            break
    print(cnt-1)