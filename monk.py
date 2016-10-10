n,k=raw_input().split()
n=int(n)
k=int(k)
str_arr=raw_input().split()
arr=[int(x)for x in str_arr]
m=0
c=0
for i in range(n):
    if arr[i]>k:
        c+=1
    else:
        m+=1
    if c==2:
        break
print m