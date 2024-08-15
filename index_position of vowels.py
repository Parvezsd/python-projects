s=input()
vc='aeiouAEIOU'
for ip in range(len(s)):
    if s[ip] in vc:
        print(ip)
#Execution:
# Take string input from user
# Creating vc variable with aeiouAEIOU as value.
# string is parvez
# iteration 1: extract p from s and check the condition p is vowel or not.
#               p is not in vowel so vc become 0
# iteration 2: extract a from s and check the condition a is vowel or not.
#               a is in vowel so vc become 1
# iteration 3: extract r from s and check the condition r is vowel or not.
#               r is not in vowel so vc become 1
# iteration 4: extract v from s and check the condition v is vowel or not.
#               v is not in vowel so vc become 1
#iteration 5: extract e from s and check the condition e is vowel or not.
#               e is in vowel so vc become 4
# iteration 6: extract z from s and check the condition z is vowel or not.
#               z is not in vowel so vc become 4
# print vowel index position is 1,4
        
