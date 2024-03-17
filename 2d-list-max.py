b=[]
for i in range(3):
    temp=[]
    for j in range(3):
        temp.append(int(input("Enter Value : ")))
    b.append(temp)
max=b[0][0]
for i in range(3):
    for j in range(3):
        if max<b[i][j]:
            max=b[i][j]
        print(b[i][j],end=" ")
    print()
print("Max = ",max)
