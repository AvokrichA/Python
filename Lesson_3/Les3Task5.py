def list_num(num_list, stop):
    nums=num_list.split(' ')
    total=0
    for x in nums:
        if x == stop:
            break
        total+= int(x)
    return total
end = '='
fin=False
n=0
while not fin:
    user_num = input('Введите числа:')
    n+= list_num(user_num, end)
    fin=end in user_num
    print(f"Sum={n}")

