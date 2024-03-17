a = list()
n = int(input("Enter N :"))
for i in range(n):
    a.append(int(input("Enter a = ")))
delete = int(input("Enter Number To Delete : "))
print(a)

for i in range(n):
    if(a[i]==delete):
        for j in range(i,n-1):
            a[j]=a[j+1]
        i-=1
        n-=1
for i in range(n):
    print(a[i])