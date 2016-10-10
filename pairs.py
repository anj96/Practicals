t=int(raw_input())
while t>0:
    t-=1
    n=int(raw_input())
    str_arr=raw_input().split()
    arr=[int(x) for x in str_arr]
    m=max(arr)-min(arr)
    max_pos=arr.count(max(arr))
    min_pos=arr.count(min(arr))
    print (min_pos*max_pos)