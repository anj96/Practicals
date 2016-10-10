import re
a=int(input())
while a>0:
    a-=1
    b=input()
    x=list()
    for i in range(len(b)):
        if (re.search("[a-z]",b[i])):
            print(b[i], end='')
        elif b[i]==")":
            y=x.pop()
            while y!="(":
                print(y, end='')
                y = x.pop()
        else:
            x.append(b[i])
    print()