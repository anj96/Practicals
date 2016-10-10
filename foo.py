a=int(input())
while a>0:
    a-=1
    b=int(input())
    x='21'
    y=str(b)
    if b%21==0:
        print('The streak is broken!')
    elif x in y:
        print('The streak is broken!')
    else:
        print('The streak lives still in our heart!')