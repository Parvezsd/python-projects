n=int(input())
space=n-1
star=1
for row in range(1,n+1):
    for space in range(1,space+1):
        print(' ',end=' ')
    for star in range(1,star+1):
        print('*',end=' ')
    print()
    space-=1
