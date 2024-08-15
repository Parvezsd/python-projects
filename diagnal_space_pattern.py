n=int(input())
space=0
star=1
for row in range(1,n+1):
    for space in range(1,space+1):
        print(' ',end=' ')
    for star in range(1,star+1):
        print('*',end=' ')
    print()
    space+=1

# Execution:
# Take input from the user
# Initially space is 0 because in the pattern there is no space so we take 0.
# Initially star is 1 because in the pattern there is 1 star so we take 1.
# we take input as 5.
# Iteration-1:- check the condition if in 1st row star is present print star.
# Iteration-2:- check the condition if in 2nd row to print how many star and space
#               is present print space 1 and star 1
# Iteration-3:- check the condition if in 3rd row to print how many star and space
#               is present print space 2 and star 1
# Iteration-4:- check the condition if in 4th row to print how many star and space
#               is present print space 3 and star 1
# Iteration-5:- check the condition if in 4th row to print how many star and space
#               is present print space 4 and star 1
# Print pattern like
# *
#  *
#   *
#    *
#     *










































































