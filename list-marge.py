a = []
b = []
c = []
n1 = int(input("Enter N1 : "))
for i in range(n1):
    a.append(int(input("Enter A : ")))
n2 = int(input("Enter N2 : "))
for i in range(n2):
    b.append(int(input("Enter B : ")))
for i in range(n1+n2):
    if i<n1:
        c.append(a[i])
    else:
        c.append(b[i-n1])
    print("c [",i,"] = ",c[i])
print(c)