n = int(input("Enter N : "))
num = n
rev = 0
while n>=1:
    rem = n%10
    rev = rev*10 + rem
    n = n//10
if(num == rev):
    print(num,"is Palindrom Number")
else:
    print(num,"is Not Palindrom Number")