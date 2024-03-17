a = int(input("Enter A : "))
b = int(input("Enter B : "))
c = int(input("Enter C : "))
d = int(input("Enter D : "))
if a<b:
    if a<c:
        if a<d:
            print("A is Min")
        else:
            print("D is Min")
    else:
        if c<d:
            print("C is Min")
        else:
            print("D is Min")
else:
    if b<c:
        if b<d:
            print("B is Min")
        else:
            print("D is Min")
    else:
        if c<d:
            print("C is Min")
        else:
            print("D is Min")
