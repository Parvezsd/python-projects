LL=int(input())
UL=int(input())
L=[]
for n in range(LL,UL+1):
    if n%2==0:
        L.append(n)
print(L[1::2])

#Execution
# Taking LL integer input from the user
# Taking UL integer input from the user
# Creating L with empty list because we are assuming that given integer might be empty
# integer in LL is 1
# integer in UL is 12
# Iteration1: extracts 1 checks conditon false doesnt enter into loop
# Iteration2: extracts 2 checks condition True Checks count condition False doesnt Prints anything
# Iteration3: extracts 3 checks conditon false doesnt enter into loop
# Iteration4: extracts 4 checks condition True Checks count condition True prints 4
# Iteration5: extracts 5 checks conditon false doesnt enter into loop
# Iteration6: extracts 6 checks condition True Checks count condition False doesnt Prints anything
# Iteration7: extracts 7 checks conditon false doesnt enter into loop
# Iteration8: extracts 8 checks condition True Checks count condition True Prints 8
# Iteration9: extracts 9 checks conditon false doesnt enter into loop
# Iteration10: extracts 10 checks condition True Checks count condition False doesnt Prints anything
# Iteration11: extracts 11 checks conditon false doesnt enter into loop
# Iteration12: extracts 12 checks condition True Checks count condition True Prints 12
# prints alternate even number as 4, 8, 12
