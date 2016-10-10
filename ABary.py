n,q=input().split()
n,q=[int(n),int(q)]
str_arr=input().split()
a=[int(x) for x in str_arr]
str_arr=input().split()
b=[int(x) for x in str_arr]
while q>0:
    q-=1
    t,l,r=input().split()
    t,l,r=[int(t),int(l)-1,int(r)]
    s=0
    if t==1:
        for i in range(l,r,2):
            s+=a[i]
        for i in range(l+1,r,2):
            s+=b[i]
    else:
        for i in range(l,r,2):
            s+=b[i]
        for i in range(l+1,r,2):
            s+=a[i]
    print(s)
