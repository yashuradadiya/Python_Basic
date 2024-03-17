name = {}
marks = {}
student = int(input("Enter Number of Students : "))
sub = int(input("Enter Number Of Subject : "))

for i in range(student):
    name['stu'+str(i)] = input("Enter Name of student"+str(i+1)+" : ")
    temp = {}
    for j in range(sub):
        temp['sub'+str(j)] = int(input("Enter Marks : "))
    marks['stu'+str(i)] = temp

total = {}
per = {}
min = {}
max = {}
result = {}
grade = {}
cnt = {}
for i in range(student):
    total['stu'+str(i)] = 0
    min['stu'+str(i)] = marks['stu'+str(i)]['sub0']
    max['stu'+str(i)] = marks['stu'+str(i)]['sub0']
    cnt['stu'+str(i)] = 0
    for j in range(sub):
        # Total marks
        total['stu'+str(i)] += marks['stu'+str(i)]['sub'+str(j)]
        # Minimum Marks
        if min['stu'+str(i)]>marks['stu'+str(i)]['sub'+str(j)]:
            min['stu'+str(i)]=marks['stu'+str(i)]['sub'+str(j)]
        # Maximum Marks
        if max['stu'+str(i)]<marks['stu'+str(i)]['sub'+str(j)]:
            max['stu'+str(i)]=marks['stu'+str(i)]['sub'+str(j)]
        # count 33 down marks
        if marks['stu'+str(i)]['sub'+str(j)]<33:
            cnt['stu'+str(i)]+=1
    # per and result
    if cnt['stu'+str(i)]==0:
        per['stu'+str(i)] = (total['stu'+str(i)]/sub)
        result['stu'+str(i)] = 'Pass'
    elif cnt['stu'+str(i)]<=2:
        per['stu'+str(i)] = 0
        result['stu'+str(i)] = 'ATKT'
    else:
        per['stu'+str(i)] = (0)
        result['stu'+str(i)] = 'Fail'
    # grade
    if per['stu'+str(i)]>=90:
        grade['stu'+str(i)] = 'Dist.'
    elif per['stu'+str(i)]>=70:
        grade['stu'+str(i)] = 'First Class'
    elif per['stu'+str(i)]>=50:
        grade['stu'+str(i)] = 'Second Class'
    elif per['stu'+str(i)]>=33:
        grade['stu'+str(i)] = 'Third Class'
    else:
        grade['stu'+str(i)] = '-'

print("Name",end='\t')
for i in range(sub):
    print('sub',i+1,end='\t')
print("total\tper\tmin\tmax\tresult  grade")

for i in range(student):
    print(name['stu'+str(i)],end='\t')
    for j in range(sub):
        print(marks['stu'+str(i)]['sub'+str(j)],end='\t')
    print(total['stu'+str(i)],end='\t')
    print(per['stu'+str(i)],end='\t')
    print(min['stu'+str(i)],end='\t')
    print(max['stu'+str(i)],end='\t')
    print(result['stu'+str(i)],end='    ')
    print(grade['stu'+str(i)])