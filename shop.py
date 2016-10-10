a=int(input())
while a>0:
    a-=1
    s=int(input())
    tot=0
    indx=99999999
    curr=0
    buy=[[0,0,0]for i in range(s)]
    for i in range(s):
        p,q,r=input().split()
        buy[i][0]=int(p)
        buy[i][1] = int(q)
        buy[i][2] = int(r)
        m=999999999999
        for j in range(3):
            if j!=indx:
                if buy[i][j]<m:
                    m=buy[i][j]
                    curr=j
        indx=curr
        tot+=buy[i][curr]
    #print(buy)
    print(tot)
