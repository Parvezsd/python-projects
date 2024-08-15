s=input()
v='aeiouAEIOU'
c=0
for i in s:
    if i.isalpha() and i not in v:
        c+=1
print(c)
#Execution:
# Take string input from user
# take another string as consonents
# Creating C variable with 0 as value because we are assuming that given string might be empty
# vowle string is aeiouAEIOU
# string is parvez
# iteration1: extract p from s and check the condition if p is in v or not.
#             p is not in v. c become 1.

# iteration2: extract a from s and check the condition if a is in v or not.
#             a is in v. c become same 1.

# iteration3: extract r from s and check the condition if r is in v or not.
#             r is not in v. c become 2.

# iteration4: extract v from s and check the condition if v is in v or not.
#             v is not in v. c become 3.

# iteration3: extract e from s and check the condition if e is in v or not.
#             e is in v. c become same 3.

# iteration3: extract z from s and check the condition if z is in v or not.
#             z is not in v. c become same 4.
# at last print c value is 4
