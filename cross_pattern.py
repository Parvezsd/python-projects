n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row ==col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#Execution:
# Take input from the user
# In Pattern program we have two types rows and colums
# We concedering outer for loop is rows and inner for loop is colums.
# Iteraion-1: check the condition if row is equal to col or not.if it true return *.
# Iteraion-2: check the condition if row is equal to col or not.if it true return *.
# Iteraion-3: check the condition if row is equal to col or not.if it true return *.
# Iteraion-4: check the condition if row is equal to col or not.if it true return *.
# Iteraion-5: check the condition if row is equal to col or not.if it true return *.
# print the output is
# *
#   *
#     *
#       *
#         *
