n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col<=n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
# Execution:-
# Taking input from the user
# Outer for loop is row and inner loop is for coloum.
# Taking input as 5.
# Iteration-1: Check the condition in 1st row how many stars and space
#              are present in 1st row 5 stars and no space.
# Iteration-2: Check the condition in 2nd row how many stars and space
#              are present in 2nd row 4 stars and 1 space.
# Iteration-3: Check the condition in 3rd row how many stars and space
#              are present in 3rd row 3 stars and 2 space.
# Iteration-4: Check the condition in 4th row how many stars and space
#              are present in 4th row 2 stars and 3 space.
# Iteration-5: Check the condition in 5th row how many stars and space
#              are present in 5th row 1 stars and 4 space.
# print pattern like
# * * * * * 
# * * * *   
# * * *     
# * *       
# *
