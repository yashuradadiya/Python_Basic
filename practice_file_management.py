# f = open('practicepractice_file_management.txt','w')
# print(f.read())
# print(f.readline(20))
# f.write("good morning\n good night\n good fternoon")
# f.write("good morning")
# f.writelines("hyy")
#f.close()

# k = [['Id:1', 'reference id:1', 'name:ved', 'email:ved@gmail.com', 'contact:7867567786'], ['Id:3', 'reference id:1', 'name:anisha', 'email:anu@gmail.com', 'contact:7867564567']]

# for i in range(len(k)):
#     f = []
#     for j in range(len(k[i])):
#         f.append(k[i][j].split(':'))
#     k[i] = f
# print(k)

# rst , psql , preety , presto , orgtbl , pipe , fancy_outline , double_outline , heavy_outline , mixed_outline , rounded_outline , simple_outline , outline , fancy_grid , mixed_grid

t = [[1, 'Apple', 'Fruits', '20'], [2, 'Mango', 'Fruits', '30'], [3, 'Tomato', 'vegetable', '20']]

from tabulate import tabulate
head = ["No.","Product Name","Category","Quntity"]
print(tabulate(t, headers=head, tablefmt="mixed_grid"))