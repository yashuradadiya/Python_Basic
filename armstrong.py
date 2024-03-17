n = int(input("Enter N : "))
num = n
sum = 0
while n>=1:
    rem = n%10
    sum = sum + (rem*rem*rem)
    n = n//10
if(num == sum):
    print(num,"is Armstrong Number")
else:
    print(num,"is Not Armstorng Number")