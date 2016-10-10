n=int(input())
while n>0:
    n-=1
    a,b=input().split()
    a,b=[int(a),int(b)]
    c=pow(a,b,10)
    #d=str(c)
    print(c)