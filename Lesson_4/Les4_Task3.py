my_list=list(range(20,241,1))
# filtred_list=[]
# for i in range(1, len(my_list)):
#      if my_list[i]%20==0 or my_list[i]%21==0:
#          filtred_list.append(my_list[i])
# print(filtred_list)

filtred_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i]%20==0 or my_list[i]%21==0]
print(filtred_list)

#Попытка2