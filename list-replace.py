a = list()
n = int(input("Enter N :"))
for i in range(n):
    a.append(int(input("Enter a = ")))
num = int(input("Enter Number To Search : "))
rep = int(input("Enter Number Of Replace : "))
print(a)
for i in range(n):
    if num==a[i]:
        a[i]=rep
print("Replace List")
print(a)