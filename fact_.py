n=int(input())
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

#Execution:
# Take integer input from user
# Creating fact variable with 1 as value because 0! is 1 thats why we take fact=1
# taking input as 5
# iteration 1: extract 1 check condition true fact is 1
# iteration 2: extract 2 check condition true fact is 2
# iteration 3: extract 3 check condition true fact is 6
# iteration 4: extract 4 check condition true fact is 24
# iteration 5: extract 5 check condition true fact is 120
# print the fact..
