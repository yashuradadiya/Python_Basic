name = []
match = []
run = []

# Get Data
def get(n):
    name.append(input("Enter Name : "))
    match.append(int(input("Enter Match : ")))
    temp = []
    for i in range(match[n]):
        temp.append(int(input("Enter Run of match "+str(i)+" = ")))
    run.append(temp)

# Count Average
def average(n):
    total = 0
    min = run[n][0]
    max = run[n][0]
    for i in run[n]:
        total += i
        if min>i:
            min = i
        if max<i:
            max = i
    per = total/match[n]
    print("Average = ",per)
    print("Minimum Run = ",min)
    print("Maximum Run = ",max)

player = int(input("Enter Plyer : "))
for i in range(player):
    get(i)
    average(i)
