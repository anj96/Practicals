a=int(input())
x=str(a)
s=0
while s>10 or s!=0:
    for i in x:
        s+=int(i)
    x=str(s)
n=a
#print(s)
p=0
while n>1:
    while n%2==0:
        #print('2', end=' ')
        p+=2
        n/=2
    for i in range(3,int(a**0.5)+1,2):
        while n%i==0:
            #print(i, end="")
            p+=i
            n/=i
    if n>2:
        p+=n
        n/=n
q=str(p)
z=0
while z>10 or z!=0:
    for i in q:
        z+=int(i)
    q=str(z)
if s==z:
    print('1')
    #print('p:'+str(p))
else:
    print('0')