from sys import argv
print(argv)
if len(argv)<3:
    print('Введите три параметра: 1.Выработка в часах, 2.Ставка в час, 3.Премия')
else:
    print(f'Salary= {int(argv[1]) * int(argv[2]) + int(argv[3])}')