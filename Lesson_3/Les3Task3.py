def list_arg(a,b,c):
    min_num = min(a,b,c)
    sum_num = a+b+c
    return sum_num-min_num

num_1=int(input('введите певрвое число:'))
num_2=int(input('Введите второе число:'))
num_3=int(input('Введите третье число:'))
my_list=[num_1, num_2, num_3]
result = list_arg(my_list[0], my_list[1], my_list[2])
print(result)




