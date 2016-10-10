t = int(input())
while t > 0:
    t -= 1
    n, l, r = input().split()
    n, l, r = [int(n), int(l), int(r)]
    str_arr = input().split()
    arr = [int(x) for x in str_arr]
    p = 0
    z = set()
    for i in arr:
        for j in range(l, r + 1):
            if j % i == 0:
                z.add(j)

    print(len(z))