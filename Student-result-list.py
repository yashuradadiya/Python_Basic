name = []
marks = []
student = int(input("Enter Number of Students : "))
sub = int(input("Enter Number Of Subject : "))

for i in range(student):
    name.append(input("Enter Name : "))
    temp=[]
    for j in range(sub):
        temp.append(int(input("Enter Marks : ")))
    marks.append(temp)

total = []
per = []
min = []
max = []
result = []
grade =[]
cnt = []
for i in range(student):
    total.append(0)
    min.append(marks[i][0])
    max.append(marks[i][0])
    cnt.append(0)
    for j in range(sub):
        total[i] += marks[i][j]
        if min[i]>marks[i][j]:
            min[i]=marks[i][j]
        if max[i]<marks[i][j]:
            max[i]=marks[i][j]
        if marks[i][j]<33:
            cnt[i]+=1
    if cnt[i]==0:
        per.append(int(total[i]/sub))
        result.append('Pass')
    elif cnt[i]<=2:
        per.append(0)
        result.append('ATKT')
    else:
        per.append(0)
        result.append('Fail')
    if per[i]>=90:
        grade.append('Dist.')
    elif per[i]>=70:
        grade.append('First Class')
    elif per[i]>=50:
        grade.append('Second Class')
    elif per[i]>=33:
        grade.append('Third Class')
    else:
        grade.append('-')

print("Name",end='\t')
for i in range(sub):
    print('sub',i+1,end='\t')
print("total\tper\tmin\tmax\tresult  grade")

for i in range(student):
    print(name[i],end='\t')
    for j in range(sub):
        print(marks[i][j],end='\t')
    print(total[i],end='\t')
    print(per[i],end='\t')
    print(min[i],end='\t')
    print(max[i],end='\t')
    print(result[i],end='    ')
    print(grade[i])