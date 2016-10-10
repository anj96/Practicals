def s(n):
    x=(n*(n+1)*((2*n)+1))/6
    return x
a=int(input())
while a!=0:
    print(int(s(a)))
    a=int(input())