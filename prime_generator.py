a=int(input())
while a>0:
    a-=1
    n, m = input().split()
    n, m = [int(n), int(m)]
    for num in range(n, m + 1):
        if num > 1:
            for i in range(2, int(num**0.5)+1):
                if (num % i) == 0:
                    break
            else:
                print(num)
