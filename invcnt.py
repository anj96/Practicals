a=int(input())
while a>0:
    a-=1
    input()
    b=int(input())
    l=[0]*b
    for i in range(b):
        l[i]=int(input())
    c=0
            
    for i in range(b):
        for j in range(i+1,b):
            if l[i]>l[j]:
                c+=1
    print(c)