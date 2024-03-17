a = list()
b = list()
n = int(input("Enter N :"))
for i in range(n):
    a.append(int(input("Enter a = ")))
for j in range(len(a)-1,-1,-1):
    b.append(a[j])

for i in range(len(b)):
    print("b [",i,"] = ",b[i])

print(a)
print(b)