import sys
def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
sys.setrecursionlimit(1100)
a=int(input())
while a>0:
    a-=1
    n,m=input().split()
    n=int(n)
    m=int(m)
    x=factorial(n+m)/(factorial(n)*factorial(m))
    print(int(x)%1000000007)
  #  print((factorial(1000)/(factorial(500)*factorial(500)))%(1000000007))