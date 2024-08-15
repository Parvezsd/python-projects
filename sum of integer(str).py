s=input()
sum=0
for i in s:
    if i.isdigit():
        k=int(i)
        sum+=k
print(sum)

#Execution:
# Take string input from user
# Creating C variable with 0 as value because we are assuming that given string might be empty
# string is 673aa456
# iteration 1: extract 6 from s and check the condition if 6 is in s or not.
#              6 is in s . C become 6
# iteration 2: extract 7 from s and check the condition if 7 is in s or not.
#               7 is in s . C become 13
# iteration 3: extract 3 from s and check the condition if 3 is in s or not.
#               3 is in s . C become 16
# iteration 4: extract a from s and check the condition if a is in s or not.
#               a is not in s . C become 16
# iteration 5: extract a from s and check the condition if a is in s or not.
#               a is not in s . C become 16
# iteration 6: extract 4 from s and check the condition if 4 is in s or not.
#               4 is in s . C become 20
# iteration 7: extract 5 from s and check the condition if 5 is in s or not.
#               5 is in s . C become 25
# iteration 8: extract 6 from s and check the condition if 6 is in s or not.
#               6 is in s . C become 31
# at last print sum is 31

