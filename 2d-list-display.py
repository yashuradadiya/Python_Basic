a = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
print(a)

b=[]
for i in range(3):
    temp=[]
    for j in range(3):
        temp.append(int(input("Enter Value : ")))
    b.append(temp)

for i in range(3):
    for j in range(3):
        print(b[i][j],end=" ")
    print()
