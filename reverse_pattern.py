n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col==n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#Execution:
# Take input from the user
# In Pattern program we have two types rows and colums
# We concedering outer for loop is rows and inner for loop is colums.
# Iteraion-1: check the condition row and colum is equal to n+1 if it is true print it
# Iteraion-2: check the condition row and colum is equal to n+1 if it is true print it
# Iteraion-3: check the condition row and colum is equal to n+1 if it is true print it
# Iteraion-4: check the condition row and colum is equal to n+1 if it is true print it
# Iteraion-5: check the condition row and colum is equal to n+1 if it is true print it
