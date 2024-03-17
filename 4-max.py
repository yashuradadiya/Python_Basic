a = int(input("Enter A : "))
b = int(input("Enter B : "))
c = int(input("Enter C : "))
d = int(input("Enter D : "))

if a>b and a>c and a>d:
    print("A is Max")
elif b>c and b>d:
    print("B is Max")
elif c>d:
    print("C is Max")
else:
    print("D is Max")
