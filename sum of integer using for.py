s=input()
sum=0
for ip in range(len(s)):
    if s[ip].isdigit():
        sum+=int(s[ip])
print(sum)
#Execution:
# Take string input from user
# Creating sum variable with 0 as value because we are assuming that given string might be empty
# string is hel3345
# iteration 1: extract h from s and check the condition if h is in s or not.
#              h is not in s . sum become 0
# iteration 2: extract e from s and check the condition if e is in s or not.
#              e is not in s . sum become 0
# iteration 3: extract l from s and check the condition if l is in s or not.
#              l is not in s . sum become 0
# iteration 4: extract 3 from s and check the condition if 3 is in s or not.
#              3 is in s . sum become 3
# iteration 5: extract 3 from s and check the condition if 3 is in s or not.
#              3 is in s . sum become 6
# iteration 6: extract 4 from s and check the condition if 4 is in s or not.
#               4 is in s . C become 10
# iteration 7: extract 5 from s and check the condition if 5 is in s or not.
#               5 is in s . C become 15
# at last print sum is 15
