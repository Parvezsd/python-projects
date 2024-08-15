n=int(input())
sp=n//2
st=1
for row in range(1,n+1):
    for sp in range(1,sp+1):
        print(' ',end=' ')
    for st in range(1,st+1):
        print('*',end=' ')
    print()
    if row<=n//2:
        st+=1
        sp-=1
    else:
        st-=1
        sp+=1
        
