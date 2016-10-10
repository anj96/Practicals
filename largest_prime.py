a=int(input())
while a>0:
    a-=1
    b=int(input())
    c=0
    num=0
    while c!=b:
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                c+=1
                #print(num)
        num+=1
    print(num-1)