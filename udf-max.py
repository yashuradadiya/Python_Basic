l = []
def max(n):
    m=l[0]
    for i in range(n):
        if m<l[i]:
            m=l[i]
    return m
n = int(input("Enter N : "))
for i in range(n):
    l.append(int(input("Enter l["+str(i)+"] = "))) 
print("Max  = ",max(n))