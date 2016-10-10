a=int(input())
while a>0:
    a-=1
    n,m=input().split()
    n,m=[int(n),int(m)]
    if n==m or m+2==n:
        if n%2==0 and m%2==0:
            print(n+m)
        elif n%2!=0 and m%2!=0:
            print(n+m-1)
        else:
            print('No Number')
    else:
        print('No Number')