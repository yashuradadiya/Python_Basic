s = []
total=0
for i in range(5):
    s.append(int(input("Enter Marks : ")))
    total+=s[i]

min=s[0]
max=s[0]
cnt=0
for i in s:
    if min>i:
        min=i
    if max<i:
        max=i
    if i<33:
        cnt+=1

if cnt==0:
    per=total/5
    result='Pass'
elif cnt<=2:
    per=0
    result='AT-KT'
else:
    per=0
    result='Fail'

if per>=90:
    grade='Dist.'
elif per>=70:
    grade='First Class'
elif per>=50:
    grade='Second Class'
elif per>=33:
    grade='Third Class'
else:
    grade='-'

print("Total = ",total)
print("Percentage = ",per)
print("Min = ",min)
print("Max = ",max)
print("Reusult = ",result)
print("Grade = ",grade)