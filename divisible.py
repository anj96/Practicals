str_arr=input()
n=int(input())
while n>0:
    n-=1
    l,r=map(int,input().split())
    z=int(str_arr[l-1:r])
    if z%7==0:
        print('YES')
    else:
        print('NO')