my_list= [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# filtred_list=[]
# for i in my_list:
#     if my_list.count(i)==1:
#         filtred_list.append(i)
# print(filtred_list)

filtred_list = [ i for i in my_list if my_list.count(i)==1]
print(filtred_list)
#Попытка2
