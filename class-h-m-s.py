class hms():
    def __init__(self) :
        self.sec = int(input("Enter Second : "))
    def logic(self):
        m = self.sec//60
        h = m//60
        m = m%60
        s = self.sec%60
        print("hour : ",h," Min : ",m," Sec : ",s)
obj = hms()
obj.logic()


