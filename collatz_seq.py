a=int(input())
d=[0]*100000000
while a>0:
    a-=1
    b=int(input())
    m = 0
    n = 0
    for i in range(b,1,-1):
        x = i
        c = 0
        if x in d:
            #print('1 '+str(x))
            break
        else:
            while x!=1:
                c+=1
            #print('y'+str(x)+str(c))
                if x%2==0:
                    x=x/2
                else:
                    x=3*x+1
                if x in d:
                    #print('2 '+str(x))
                    c+=d[int(x)]
                    break
                else:
                    continue
            d[int(x)]=c
                #print(x)
        #if c>m:
            #m=c
            #n=i
    #print(max(d))
    #print(max(d, key=d.get))
    #m=0
    #q=0
    #for i,k in d.items():
    #    if k>=m and i<b:
    #        m=k
     #       q=i
    print(max(d))

