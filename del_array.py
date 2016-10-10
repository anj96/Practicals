import collections
a=int(input())
str_arr=input().split()
arr=[int(x) for x in str_arr]
x=[count for item, count in collections.Counter(arr).items() ]
y=[item for item, count in collections.Counter(arr).items() ]
m=x.index(max(x))
e=y[m]
c=0
for i in arr:
    if i ==e:
        continue
    else:
        c+=1

print(c)
