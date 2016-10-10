n,q=input().split()
n=int(n)
q=int(q)
str_arr=input().split()
a=[int(x) for x in str_arr]
while q>0:
    q-=1
    arr = [int(x) for x in str_arr]
    #print(arr)
    l, r = input().split()
    l = int(l)-1
    r = int(r)-1
    c = 0
    for i in range(l,r+1):
        #print(l)
        while arr[i]>1:
            c+=1
            arr[i]=int(arr[i]/2)
            #print(arr[i])
        if arr[i]==1 and i!=r:
            arr[i]=0
        elif arr[i]==1 and i==r:
            print('h')
            arr[i]=0
            if c%2!=0:
                print('Mishki')
            else:
                print('Hacker')