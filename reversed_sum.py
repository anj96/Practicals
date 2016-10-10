a=int(input())
while a>0:
    a-=1
    n, m = input().split()
    #n, q = [int(n), int(q)]
    #print(n)
    c=n[::-1]
    d=m[::-1]
    e=int(c)+int(d)
    e=str(e)
    f=e[::-1]
    f=int(f)
    print(f)