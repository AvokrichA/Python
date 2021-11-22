def fact(num):
    num_1 = 1
    for i in range(1, num + 1):
        num_1 *= i
        yield num_1
x = 10
for y, z in enumerate(fact(x)):
    print(f'!{y+1} {z}')
#попытка2
