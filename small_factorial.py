def fa(n):
    if n==0:
        return 1
    else:
        return n*fa(n-1)
a=int(input())
while a>0:
    a-=1
    b=int(input())
    print(fa(b))