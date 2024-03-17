a=[]
for i in range(3):
    temp=[]
    for j in range(3):
        temp.append(int(input("Enter Value : ")))
    a.append(temp)

for i in range(3):
    sum=0
    for j in range(3):
        print(a[i][j],end=' ')
        sum += a[i][j]
    print("=",sum)