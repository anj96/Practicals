p,q,r=input().split()
p,q,r=[int(p),int(q),int(r)]
while p>q or p<q:
    if r - q == q - p:
        print('AP ' + str(r + (r - q)))
    else:
        print('GP ' + str(int((r / q) * r)))
    p,q,r=input().split()
    p,q,r=[int(p),int(q),int(r)]
