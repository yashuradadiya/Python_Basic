a=[]
for i in range(3):
    temp=[]
    for j in range(3):
        temp.append(int(input("Enter Value : ")))
    a.append(temp)
sum=[]
for i in range(3):
    sum.append(0)
    for j in range(3):
        print(a[i][j],end=' ')
        sum[i] += a[j][i]
    print()
for i in sum:
    print(i,end=' ')