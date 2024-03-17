n = int(input("Enter N : "))
fact = 1
while n>=1:
    print(n,end="")
    if n>1:
        print(" * ",end="")
    else:
        print(" = ",end="")
    fact*=n
    n-=1
print(fact)