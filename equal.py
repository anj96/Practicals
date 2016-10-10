def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a
a=int(input())
while a>0:
    a-=1
    n,x,y,z=input().split()
    n,x,y,z=[int(n),int(x),int(y),int(z)]
    str_arr=input().split()
    arr=[int(x)for x in str_arr]
    p=0
    for i in arr:
        if gcd(i,x) or gcd(i,y) or gcd(i,z)==1:
            print(gcd(i,z))
            print("She Can't")
            p=1
            break
    if p==0:
        print("She can")
