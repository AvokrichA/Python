from itertools import count, cycle

for i in count(3):
    if i>10:
        break
    print(i)

my_list = [3, 15, 18, 42]
counter = 0
for i in cycle(my_list):
    counter += 1
    if counter > 10:
        break
    print(i)

#попытка2