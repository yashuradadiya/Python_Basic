class area():
    PI = 3.14
    def circle(self):
        r = int(input("Enter Radius : "))
        area = self.PI * r * r
        return area
    def square(self):
        l = int(input("Enter Side : "))
        area = l * l
        return area
    def rectengle(self):
        l = int(input("Enter Length : "))
        b = int(input("Enter Height : "))
        area = l * b
        return area

print("1. Area Of Circle : ")
print("2. Area Of Square : ")
print("3. Area Of Recetengel : ")
print("0. Exit")
ch = 1
while ch!=0:
    ch = int(input("Enter Your Choice : "))
    obj = area()
    if ch==1:
        print("Area Of Circle = ",obj.circle())
    elif ch==2:
        print("Area Of Square = ",obj.square())
    elif ch==3:
        print("Area Of Rectengle = ",obj.rectengle())
    else :
        print("Enter Valid Choice")
