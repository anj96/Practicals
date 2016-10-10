a = int(input())
def gcd(p,q):
    while q!=0:
        t=p%q
        p=q
        q=t
    return p
mul = 1
while a > 0:
    a -= 1
    b = int(input())
    for i in range(1, b + 1):
        if mul % i != 0:
            x=i/gcd(mul,i)
            mul = mul * x
    print(mul)
