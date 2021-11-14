# Вариант решения-1

# def deg_arg(a,b):
#     return pow(a, b)
# num_1=float(input('Введите целое положительное число:'))
# num_2=int(input('Введите целое отрицательное число:'))
#
# result = deg_arg(num_1, num_2)
# print(result)]

# Вариант решения-2

def deg_arg(a,b):
    return a**b
num_1=float(input('Введите целое положительное число:'))
num_2=int(input('Введите целое отрицательное число:'))

result = deg_arg(num_1, num_2)
print(result)