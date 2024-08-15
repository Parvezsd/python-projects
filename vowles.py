v='aeiouAEIOU'
s=input()
c=0
for i in s:
    if i in v:
        c+=1
print(c)

#Execution:
# Take string input from user
# take another string as vowles
# Creating C variable with 0 as value because we are assuming that given string might be empty
# vowle string is aeiouAEIOU
# string is parvez
# iteration1: extract p from s and check the condition if p is in v or not.
#             p is not in v. c become 0
# iteration2: extract a from s and check the condition if a is in v or not.
#             a is in v. c become 1
# iteration3: extract r from s and check the condition if r is in v or not.
#             r is not in v. c become same 1.
# iteration4: extract v from s and check the condition if v is in v or not.
#             v is not in v. c become same 1.
# iteration3: extract e from s and check the condition if e is in v or not.
#             e is in v. c become same 2.
# iteration3: extract z from s and check the condition if z is in v or not.
#             z is not in v. c become same 2.
# at last print c value is 2

