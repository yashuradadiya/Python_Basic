a=[]
print("First Array")
for i in range(3):
    temp=[]
    for j in range(3):
        temp.append(int(input("Enter Value : ")))
    a.append(temp)
b=[]
print("Second Array")
for i in range(3):
    temp=[]
    for j in range(3):
        temp.append(int(input("Enter Value : ")))
    b.append(temp)
c=[]
for i in range(3):
    temp=[]
    for j in range(3):
        temp.append(a[i][j]+b[i][j])
    c.append(temp)
for i in range(3):
    for j in range(3):
        print(c[i][j],end=' ')
    print()