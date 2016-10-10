import collections
a=input()
sarr=list(a)
arr=[count for item, count in collections.Counter(sarr).items() ]
c=0
s=0
print(arr)
m1=arr.count(max(arr))
m2=arr.count(min(arr))
d1=max(arr)
d2=min(arr)
print(m1)
print(m2)
print(d1)
print(d2)
if d1==d2:
    print('YES')
elif d2==1 and m2==1:
    print('YES')
elif d1==1 and m1==1:
    print('YES')
elif d2+1==d1:
    if m2==1:
        print('YES')
    elif m1==1:
        print('YES')
    else:
        print('NO')
else:
    print('No')