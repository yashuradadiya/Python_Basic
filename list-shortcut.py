a = [10,20,30,40,50]
print("a = ",a)
a.insert(2,999)
print("Inserted a = ",a)

b = [10,20,30,40,50]
print("b = ",b)
b.remove(30)
print("Removed b = ",b)

a.clear()
print("Cleared = ",a)

del b
print("Deleted = ",b)