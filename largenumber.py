import collections
n=int(input())
str_arr=input().split()
arr=[int(x) for x in str_arr]
q=int(input())
d = {x: arr.count(x) for x in arr}
print(d.keys())
print(d)
#while q>0:
#    q-=1
#    t,x=input().split(' ')
#    t=int(t)
#    x=int(x)
