n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row<=col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#Execution:-
# Take input from the user
# outer loop is for row and inner loop is coloum
# take input is as 5
# check the condition to print how many stars and space present in
# row
# Iteration-1:check the condition to print how many stars and space present in     
#             stars is 5 and space is 0.
# Iteration-2:check the condition to print how many stars and space present in     
#             stars is 4 and space is 1.
# Iteration-3:check the condition to print how many stars and space present in     
#             stars is 3 and space is 2.
# Iteration-4:check the condition to print how many stars and space present in     
#             stars is 2 and space is 3.
# Iteration-45check the condition to print how many stars and space present in     
#             stars is 1 and space is 4.
# print the pattern like

#* * * * * 
#  * * * * 
#    * * * 
#      * * 
#        * 
