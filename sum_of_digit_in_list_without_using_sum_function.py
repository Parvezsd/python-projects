'''L=eval(input())
sum=0
for i in L:
    sum+=i
print(sum)
'''
L=eval(input())
sum=0
for k in L:
    if isinstance(k,int):
        sum+=k
print(sum)
#Execution:
# Take list input from user
# Creating sum variable with 0 as value because we are assuming that given list might be empty
# list is [11,22,33] 
# iteration 1: extract 11 from L and check the condition if 11 is in L or not.
#              11 is in L .sum become 11
# iteration 2: extract 22 from L and check the condition if 22 is in L or not.
#              22 is in L .sum become 33
# iteration 3: extract 33 from L and check the condition if 33 is in L or not.
#              33 is in L .sum become 66
#print sum become 66.
