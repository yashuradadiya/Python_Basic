sub = []
# Get Marks
def subject():
    for i in range(5):
        sub.append(int(input("Enter sub "+str(i+1)+" : ")))
# total
def total():
    t=0
    for i in range(5):
        t += sub[i]
    return t
# minimum
def minimum():
    m=sub[0]
    for i in range(5):
        if m>sub[i]:
            m=sub[i]
    return m
# maximum
def maximum():
    m=sub[0]
    for i in range(5):
        if m<sub[i]:
            m=sub[i]
    return m
def count():
    cnt = 0
    for i in sub:
        if i<33:
            cnt+=1
    return cnt
def percentge(cnt,total):
    if cnt==0:
        per = total/5
    else:
        per = 0
    return per
def result(cnt):
    if cnt==0:
        result = "PASS"
    elif cnt<=2:
        result = "ATKT"
    else:
        result = "FAIL"
    return result
def grade(per):
    if per>=80:
        g = "Dict."
    elif per>=65:
        g = "First Class"
    elif per>=50:
        g = "Second Class"
    elif per>=33:
        g = "Third Class"
    else:
        g = "-"
    return g
subject()
c = count()
t = total()
print('Total = ',t)
print("Minimum = ",minimum())
print("Maximum = ",maximum())
p = percentge(c,t)
print("Percentge = ",p)
print("Result = ",result(c))
print("Grade = ",grade(p))


