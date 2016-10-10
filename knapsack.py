a=int(input())
while a>0:
    a-=1
    n,k=input().split()
    n,k=[int(n),int(k)]
    str_arr=input().split()
    arr=[int(x)for x in str_arr]
    ways=[0]*(k+1)
    for i in range(1,k+1):
        for j in range(0,n):
            if arr[j]<=i:
                ways[i]=max(ways[i],arr[j]+ways[i-arr[j]])
    print(ways[k])