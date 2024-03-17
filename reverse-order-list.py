a = list()
n = int(input("Enter N :"))
for i in range(n):
    a.append(int(input("Enter a = ")))
for j in range(len(a)-1,-1,-1):
    print("a [",j,"] = ",a[j])
