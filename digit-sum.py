n = int(input("Enter N : "))
sum = 0
while n>=1:
    rem = n%10
    sum = sum + rem 
    n=n//10
print("Sum = ",sum)