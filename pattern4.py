n = int(input("Enter N : "))
for i in range(n,0,-1):
    for j in range(n,i-1,-1):
        print(j,end=" ")
    print()