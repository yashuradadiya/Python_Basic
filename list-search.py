a = list()
n = int(input("Enter N :"))
for i in range(n):
    a.append(int(input("Enter a = ")))
num = int(input("Enter Number To Search : "))
print(a)
for i in range(n):
    if num==a[i]:
        pos=i
        
print(num,"is on position : ",pos)