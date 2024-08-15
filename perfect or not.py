n=int(input())
ds=0
for i in range(1,n//2+1):
    if n%i==0:
        ds+=i
if ds==n:
    print('n is perfect number')
else:
    print('n is not perfect number')
# Execution:-
# Taking integer input from the user
# Creating ds value becomes '0' because assume that ds is initially '0'
# integer is 6
# iteratin-1: Extract 1 and check the condition 6%i==0,it is true ds value become 1
# iteratin-2: Extract 2 and check the condition 6%i==0,it is true ds value become 3
# iteratin-3: Extract 3 and check the condition 6%i==0,it is true ds value become 6
# iteratin-4: Extract 4 and check the condition 6%i==0,it is not true ds value become 6
# iteratin-5: Extract 5 and check the condition 6%i==0,it is not true ds value become 6
# iteratin-6: Extract 6 and check the condition 6%i==0,it is not true ds value become 6
# At last print ds value as 6
