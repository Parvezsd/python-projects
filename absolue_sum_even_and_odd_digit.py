s=input()
es=0
os=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            es+=k
        else:
            os+=k
print(abs(es-os))
#Execution:
# Take string input from user
# Creating es(even sum) variable with 0 as value because we are assuming that given string might be empty
# Creating os(odd sum) variable with 0 as value because we are assuming that given string might be empty
# string is he9324
# iteration 1: extract h from s and check the condition if h is in s or not.
#              h is not in s . es become 0
# iteration 2: extract e from s and check the condition if e is in s or not.
#              e is not in s . es become 0
# iteration 3: extract 9 from s and check the condition if 9 is in s or not.
#              9 is in s . os become 9
# iteration 4: extract 3 from s and check the condition if 3 is in s or not.
#              3 is in s . os become 12
# iteration 5: extract 2 from s and check the condition if 2 is in s or not.
#              2 is in s . es become 2
# iteration 6: extract 4 from s and check the condition if 4 is in s or not.
#              4 is in s . es become 6
# print difference between es and odd sum

