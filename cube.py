n = int(input("Enter N : "))
while n>=1:
    rem = n%10
    cube = rem * rem * rem
    print(rem," = ",cube)
    n=n//10