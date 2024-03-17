a = list()
n = int(input("Enter N :"))
for i in range(n):
    a.append(int(input("Enter a = ")))
print(a)
min = a[0]
for i in a:
    if min>i:
        min=i
print("Min = ",min)