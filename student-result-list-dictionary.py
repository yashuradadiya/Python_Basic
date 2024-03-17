name = {}
marks = {}
student = int(input("Enter Number of Students : "))
sub = int(input("Enter Number Of Subject : "))

for i in range(student):
    name[i] = input("Enter Name of student"+str(i+1)+" : ")
    temp = {}
    for j in range(sub):
        temp[j] = int(input("Enter Marks : "))
    marks[i] = temp

total = {}
per = {}
min = {}
max = {}
result = {}
grade = {}
cnt = {}
for i in range(student):
    total[i] = 0
    min[i] = marks[i][0]
    max[i] = marks[i][0]
    cnt[i] = 0
    for j in range(sub):
        # Total marks
        total[i] += marks[i][j]
        # Minimum Marks
        if min[i]>marks[i][j]:
            min[i]=marks[i][j]
        # Maximum Marks
        if max[i]<marks[i][j]:
            max[i]=marks[i][j]
        # count 33 down marks
        if marks[i][j]<33:
            cnt[i]+=1
    # per and result
    if cnt[i]==0:
        per[i] = (total[i]/sub)
        result[i] = 'Pass'
    elif cnt[i]<=2:
        per[i] = 0
        result[i] = 'ATKT'
    else:
        per[i] = (0)
        result[i] = 'Fail'
    # grade
    if per[i]>=90:
        grade[i] = 'Dist.'
    elif per[i]>=70:
        grade[i] = 'First Class'
    elif per[i]>=50:
        grade[i] = 'Second Class'
    elif per[i]>=33:
        grade[i] = 'Third Class'
    else:
        grade[i] = '-'

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