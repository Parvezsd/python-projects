s=input()
c='aeiouAEIOU'
for ip in range(len(s)):
    if s[ip].isalpha() and s[ip] not in c:
        print(s[ip])
#Execution:
# Take string input from user
# Creating c variable with aeiouAEIOU as value.
# string is parvez
# iteration 1: extract p from s and check the condition p is vowel or not.
#               p is not in vowel so c become 0
# iteration 2: extract a from s and check the condition a is vowel or not.
#               a is in vowel so c become nothing
# iteration 3: extract r from s and check the condition r is vowel or not.
#               r is not in vowel so c become 2
# iteration 4: extract v from s and check the condition v is vowel or not.
#               v is not in vowel so c become 3
#iteration 5: extract e from s and check the condition e is vowel or not.
#               e is in vowel so c become nothing
# iteration 6: extract z from s and check the condition z is vowel or not.
#               z is not in vowel so c become 5
# print c index position is 0,2,3,5
