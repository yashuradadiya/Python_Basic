n1 = int(input("Enter N1 : "))
n2 = int(input("Enter N2 : "))
if n1<n2:
    while n1<=n2:
        if n1%2==1:
            print(n1)
        n1+=1
else:
    while n1>=n2:
        if n1%2==0:
            print(n1)
        n1-=1