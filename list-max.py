a = list()
n = int(input("Enter N :"))
for i in range(n):
    a.append(int(input("Enter a = ")))
print(a)
max = a[0]
for i in a:
    if max<i:
        max=i
print("Min = ",max)