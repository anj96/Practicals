import collections
str_arr=input().split()
a=[int(x)for x in str_arr]
x=[count for item, count in collections.Counter(a).items()]
print(x)