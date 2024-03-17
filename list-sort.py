n = int(input("Enter N : "))
a = []
for i in range(n):
    a.append(int(input("Enter Value : ")))

for i in range(n):
    for j in range(0, n-i-1):
        if a[j]>a[j+1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp

print("Sorted array:", a)
