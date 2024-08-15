s=input()
v='aeiouAEIOU'
vc=0
cc=0
for i in s:
    if i.isalpha():
        if i in v:
            vc+=1
        else:
            cc+=1
print(vc)
print(cc)

#Execution:
# Take string input from user
# take another string as vowles
# Creating VC variable with 0 as value because we are assuming that given string might be empty
# Creating CC variable with 0 as value because we are assuming that given string
# vowle string is aeiouAEIOU
# string is parvez
# iteration1: extract p from s and check the condition if p is in v.
#             p is not in v. cc become 1
# iteration2: extract a from s and check the condition if a is in v or not.
#             a is in v. vc become 1
# iteration3: extract r from s and check the condition if r is in v or not.
#             r is not in v. cc become 2.
# iteration4: extract v from s and check the condition if v is in v or not.
#             v is not in c. cc become 3.
# iteration3: extract e from s and check the condition if e is in v or not.
#             e is in v. vc become 2.
# iteration3: extract z from s and check the condition if z is in v or not.
#             z is not in v. cc become same 4.
# at last print cc value is 4
# at last print vc value is 2

