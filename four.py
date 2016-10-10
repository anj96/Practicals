a = int(input())
while a > 0:
    a -= 1
    b = int(input())
    c = str(b)
    cnt = 0
    for i in range(len(c)):
        if c[i] == '4':
            cnt += 1
        else:
            pass
    print(cnt)