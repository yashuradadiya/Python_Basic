a = list()
sum=0
n = int(input("Enter N :"))
for i in range(n):
    a.append(int(input("Enter a = ")))
    sum+=a[i]
print(a)
print("Sum = ",sum)