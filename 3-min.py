a = int(input("Enter A : "))
b = int(input("Enter B : "))
c = int(input("Enter C : "))
if a<b:
    if a<c:
        print("A is Min")
    else:
        print("C is Min")
else:
    if b<c:
        print("B is Min")
    else:
        print("C is Min")
