class B:
    def get(s):
        s.m=2000
        s.r = 2.3
        s.n = 2
class c(B):
    def cls(s):
        si = (s.m*s.r*s.n)/100
        print(si)
obj = c()
obj.get()
obj.cls()