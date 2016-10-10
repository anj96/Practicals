d={0:0}
def exchange(n):
    if n in d:
        return d[n]
    else:
        d[n]=max(n,(exchange(n//4)+exchange(n//3)+exchange(n//2)))
        return d[n]
while True:
    try:
        print(exchange(int(input())))
    except:
        break