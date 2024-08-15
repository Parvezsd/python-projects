LL=int(input())
UL=int(input())
c=0
for n in range(LL,UL+1):
    if n%2==0:
        c+=1
        if c%2!=0:
            print(n)
#Execution
'''
1-> Taking lower limit from the user
2-> Taking upper limit from the user
3-> taking input LL as 1 and UL as 12
4-> iteration starts
    Iteration1: extracts 1 checks conditon false doesnt enter into loop
    Iteration2: extracts 2 checks condition True Checks count condition True prints 2
    Iteration3: extracts 3 checks conditon false doesnt enter into loop
    Iteration4: extracts 4 checks condition True Checks count condition False doesnt Prints anything
    Iteration5: extracts 5 checks conditon false doesnt enter into loop
    Iteration6: extracts 6 checks condition True Checks count condition True prints 6
    Iteration7: extracts 7 checks conditon false doesnt enter into loop
    Iteration8: extracts 8 checks condition True Checks count condition False doesnt Prints anything
    Iteration9: extracts 9 checks conditon false doesnt enter into loop
    Iteration10: extracts 10 checks condition True Checks count condition True prints 10
    Iteration11: extracts 11 checks conditon false doesnt enter into loop
    Iteration12: extracts 12 checks condition True Checks count condition False doesnt Prints anything
5-> prints alternate even number as 4, 8, 12'''

