match = []
name= []
run = []
class score():
    def get(self,n):
        name.append("Enter Name : ")
        match.append("Enter Match : ")
        temp = []
        for i in range(match[n]):
            temp.append("Enter run of match"+str(i+1)+" : ")
        run.append(temp)

    def average(self,n):
        total = 0 
        for i in run[n]:
            total += i
        return total
    
    def minimum(self,n):
        m = run[n][0]
        for i in run[n]:
            if m>i:
                m = i
        return m
    
    def maximum(self,n):
        m = run[n][0]
        for i in run[n]:
            if m<i:
                m = i
        return m
    
    