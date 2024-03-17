n = int(input("Enter N : "))
cnt=0
while n>=1:
    rem = n%10
    cnt+=1
    n=n//10
print("Number Of Digit : ",cnt)