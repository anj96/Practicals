def f(n):
    if n==0:
        return 1
    else:
        return n*f(n-1)
n=int(input())
while n>0:
    n-=1
    a,b,c=input().split()
    a,b,c=[int(a),int(b),int(c)]
    if (a+b)<=c:
        print('1/1')
    else:
        e=0
        d=f(a)+1+f(b)+1
        for i in range(a+1):
            for j in range(b+1):
                g=i+j
                if g>=c:
                    e+=1
        m=e/d
        print(e)
        print(d)
        print(m)