my_list= [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# filtred_list=[]
# for i in range(1, len(my_list)):
#     if my_list[i]>my_list[i-1]:
#         filtred_list.append(my_list[i])
# print(filtred_list)


filtred_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i]>my_list[i-1]]
print(filtred_list)
