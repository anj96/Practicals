a=int(input())
while a>0:
    a-=1
    b=int(input())
    cnt=0
    while b/5>0:
        cnt+=b//5
        b=b//5
    print(cnt)
