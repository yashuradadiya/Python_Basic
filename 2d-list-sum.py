b=[]
for i in range(3):
    temp=[]
    for j in range(3):
        temp.append(int(input("Enter Value : ")))
    b.append(temp)
sum = 0
for i in range(3):
    for j in range(3):
        print(b[i][j],end=" ")
        sum += b[i][j]
    print()

print("Sum : ",sum) 
