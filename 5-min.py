a = int(input("Enter A : "))
b = int(input("Enter B : "))
c = int(input("Enter C : "))
d = int(input("Enter D : "))
e = int(input("Enter E : "))
if a<b:
    if a<c:
        if a<d:
            if a<e:
                print("A is Min")
            else:
                print("E is Min")
        else:
            if d<e:
                print("D is Min")
            else:
                print("E is Min")
    else:
        if c<d:
            if c<e:
                print("C is Min")
            else:
                print("E is Min")
        else:
            if d<e:
                print("D is Min")
            else:
                print("E is Min")
else:
    if b<c:
        if b<d:
            if b<e:
                print("B is Min")
            else:
                print("E is Min")
        else:
            if d<e:
                print("D is Min")
            else:
                print("E is Min")
    else:
        if c<d:
            if c<e:
                print("C is Min")
            else:
                print("E is Min")
        else:
            if d<e:
                print("D is Min")
            else:
                print("E is Min")
