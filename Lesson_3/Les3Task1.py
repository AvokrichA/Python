
def num_list_div(x, y):
    if y==0:
        return "На 0 делить нельзя!"
    else:
        return x / y

x=float(input('Введите делимое:'))
y=float(input('Введите делитель:'))

print(num_list_div(x, y))



