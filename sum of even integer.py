s=input()
sum=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            sum+=k
print(sum)

#Execution:
# Take string input from user
# Creating sum variable with 0 as value because we are assuming that given string might be empty
# string is hello426
# iteration 1: extract h from s and check the condition if h is in s or not.
#              h is not in s . sum become 0
# iteration 2: extract e from s and check the condition if e is in s or not.
#              e is not in s . sum become 0
# iteration 3: extract l from s and check the condition if l is in s or not.
#              l is not in s . sum become 0
# iteration 4: extract l from s and check the condition if l is in s or not.
#              l is not in s . sum become 0
#iteration 5: extract o from s and check the condition if o is in s or not.
#              o is not in s . sum become 0
# iteration 6: extract 4 from s and check the condition if 4 is in s or not.
#              4 is in s . sum become 4
# iteration 7: extract 2 from s and check the condition if 2 is in s or not.
#              2 is in s . sum become 6
# iteration 8: extract 6 from s and check the condition if 6 is in s or not.
#              6 is in s . sum become 12
# print sum is 12


