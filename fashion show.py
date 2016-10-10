a=int(input())
while a>0:
    a-=1
    b=int(input())
    str_arr=input().split()
    x=[int(z)for z in str_arr]
    str_arr = input().split()
    y = [int(z) for z in str_arr]
    x.sort()
    y.sort()
    h=0
    for i in range(b):
        h+=x[i]*y[i]
    print(h)
