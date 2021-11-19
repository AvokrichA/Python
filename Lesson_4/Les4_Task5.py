from functools import reduce
# num_list=[]
# for i in range(100,1001):
#     if i%2==0:
#         num_list.append(i)
#         total=reduce(lambda x, y: x * y, num_list)
# print(total)

num_list=[i for i in range(100,1001) if i%2==0]
total=reduce(lambda x, y: x * y, num_list)
print(total)