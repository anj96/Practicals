str_arr=input().split()
arr=[int(x)for x in str_arr]
x=len(arr)
lheight=[0]*x
rheight=[0]*x
m=[0]*x
water=0
for i in range(1,len(arr)-1):
    lheight[i]=max(arr[:i+1])
    rheight[i]=max(arr[i:])
    m[i]=min(lheight[i],rheight[i])
    water+=m[i]-arr[i]

print(lheight)
print(rheight)
print(m)
print(arr)
print(water)