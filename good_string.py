a=int(input())
while a>0:
    a-=1
    s=input()
    x=str(s[0])
    for i in range(0,len(s)-1):
        if s[i]!=s[i+1]:
            x+=str(s[i+1])
    print(x)