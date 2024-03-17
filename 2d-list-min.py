b=[]
for i in range(3):
    temp=[]
    for j in range(3):
        temp.append(int(input("Enter Value : ")))
    b.append(temp)
min=b[0][0]
for i in range(3):
    for j in range(3):
        if min>b[i][j]:
            min=b[i][j]
        print(b[i][j],end=" ")
    print()
print("Min = ",min)