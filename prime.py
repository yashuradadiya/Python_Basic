n = int(input("Enter N : "))
cnt=0
for i in range(2,n):
    if n%i==0:
        cnt+=1
if cnt==0:
    print(n,"is Prime Number")
else:
    print(n,"is Not Prime Number")
