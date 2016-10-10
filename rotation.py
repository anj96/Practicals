def rrotate(l,n):
    return l[-n:] + l[:-n]
def lrotate(l,n):
    return l[n:] + l[:n]

n,k=raw_input().split()
n=int(n)
k=int(k)
str_arr=raw_input().split()
arr=[int(x)for x in str_arr]
str_tarr=raw_input().split()
tarr=[int(x)for x in str_tarr]
id=0
for i in range(k):
    r, l = raw_input().split()
    l = int(l)
    id+=1
    if r=='R':
        arr=rrotate(arr,l)
    else:
        arr=lrotate(arr,l)
    if arr==tarr:
        print id
        break
