a = int(input("Enter A : "))
b = int(input("Enter B : "))
c = int(input("Enter C : "))
d = int(input("Enter D : "))
e = int(input("Enter E : "))

if a>b and a>c and a>d and a>e:
    print("A is Max")
elif b>c and b>d and b>e:
    print("B is Max")
elif c>d and c>e:
    print("C is Max")
elif d>e:
    print("D is Max")
else:
    print("E is Max")
