s1 = int(input("Enter Marks of s1 : "))
s2 = int(input("Enter Marks of s2 : "))
s3 = int(input("Enter Marks of s3 : "))
s4 = int(input("Enter Marks of s4 : "))
s5 = int(input("Enter Marks of s5 : "))

total = s1 + s2 + s3 + s4 + s5

if s1<s2 and s1<s3 and s1<s4 and s1<s5:
    min_m = s1
elif s2<s3 and s2<s4 and s2<s5:
    min_m = s2
elif s3<s4 and s3<s5:
    min_m = s3
elif s4<s5:
    min_m = s4
else:
    min_m = s5

if s1>s2 and s1>s3 and s1>s4 and s1>s5:
    max_m = s1
elif s2>s3 and s2>s4 and s2>s5:
    max_m = s2
elif s3>s4 and s3>s5:
    max_m = s3
elif s4>s5:
    max_m = s4
else:
    max_m = s5

cnt=0;
if s1<35:
    cnt+=1   
if s2<35:
    cnt+=1
if s3<35:
    cnt+=1
if s4<35:
    cnt+=1
if s5<35:
    cnt+=1

if cnt==0:
    result = "PASS"
    per = total/5;
elif cnt<=2:
    result = "ATKT"
    per = 0;
else :
    result = "FAIL"
    per = 0;

if per>80:
    grade = "First Class"
elif per>60:
    grade = "Second Class"
elif per>35:
    grade = "Third Class"
else:
    grade = "-"
print("Total = ",total)
print("Per. = ",per)
print("Minimum Marks = ",min_m)
print("Maximum Marks = ",max_m)
print("Result = ",result)
print("grade = ",grade)
