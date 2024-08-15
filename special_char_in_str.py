s=input()
c=0
for i in s:
    if not i.isalnum():
        c+=1
print(c)

#Execution:
# Take string input from user
# Creating sum variable with 0 as value because we are assuming that given string might be empty
# string is he@&*
# iteration 1: extract h from s and check the condition if h is in s or not.
#              h is not in s . special character c become 0
# iteration 2: extract e from s and check the condition if h is in s or not.
#              e is not in s . special character c become 0
# iteration 3: extract @ from s and check the condition if h is in s or not.
#              @ is in s . special character c become 1
# iteration 4: extract & from s and check the condition if h is in s or not.
#              & is in s . special character c become 2
# iteration 5: extract * from s and check the condition if h is in s or not.
#              * is in s . special character c become 3
# print special character sum.
