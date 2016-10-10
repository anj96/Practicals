a=int(input())
while a!=0:
    s=input()
    k=0
    #print(len(s))
    x=['' for i in range(int(len(s)/a))]
    for i in range(0,len(s),a):
        if k%2==0:
            for j in range(a):
                x[k]+=s[i+j]
        else:
            for j in range(a-1,-1,-1):
                x[k]+=s[i+j]
        k+=1
    #print(x)
    for j in range(a):
        for i in range(int(len(s)/a)):
            print(x[i][j], end='')
    print()

    a=int(input())