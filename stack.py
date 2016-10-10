a=int(input())
x=list()
while a>0:
    a-=1
    p=input()
    #print(p)
    if p[0]=='1':
        s=int(p[2:])
        #print(p[0])
        x.append(s)
    elif p[0]=='2':
        x.pop()
    else:
        print(max(x))
    #print(x)