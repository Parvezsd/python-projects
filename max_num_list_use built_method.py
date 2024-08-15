L=eval(input())
max=0
for i in L:
    if i > max:
        max=i
print(max)
#Execution:
# Take list input from user
# Creating sum variable with 0 as value because we are assuming that given list might be empty
# list is [11,22,100] 
# iteration 1: extract 11 from L and check the condition if 11 is in L or not.
#              11 is in L .max become 0
# iteration 2: extract 22 from L and check the condition if 22 is in L or not.
#              22 is in L .max become 0
# iteration 3: extract 100 from L and check the condition if 100 is in L or not.
#              100 is in L .max become 100

#print max become 100.
