a = list()
b =list()
n = int(input("Enter N :"))
for i in range(n):
    a.append(int(input("Enter a = ")))
    
pos = int(input("Enter Position  : "))
num = int(input("Enter Number To Add : "))
print(a)

for i in range(n+1):
    if i<pos:
        b.append(a[i])
    elif i==pos:
        b.append(num)
    else:
        b.append(a[i-1])
print(b)
# for i in range(n-1,pos-1,-1):
#     a[i+1]=a[i]
#     print(a[i])
# a[pos]=num
# print(a)