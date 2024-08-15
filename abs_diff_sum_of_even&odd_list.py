l=eval(input())
es=0
os=0
for i in l:
    if i%2==0:
        es+=i
    else:
        os+=i
print(abs(es-os))
#Execution:
# Take list input from user
# Creating es(even sum) variable with 0 as value because we are assuming that given list might be empty
# Creating os(odd sum) variable with 0 as value because we are assuming that given list might be empty
# list is [11,22,33,44]
# iteration 1: extract 11 from l and check the condition if 11 is in l or not.
#              11 is in l . os become 11
# iteration 2: extract 22 from l and check the condition if 22 is in l or not.
#              22 is in l . es become 22
# iteration 3: extract 33 from l and check the condition if 33 is in l or not.
#              33 is in s . os become 33
# iteration 4: extract 44 from l and check the condition if 44 is in l or not.
#              44 is in l . es become 44

# print difference between es and odd sum
