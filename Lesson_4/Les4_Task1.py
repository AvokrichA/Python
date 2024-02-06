from sys import argv
print(argv)
if len(argv)<3:
    print('Введите три параметра: 1.Выработка в часах, 2.Ставка в час, 3.Премия')
else:
    print(f'Salary= {float(argv[1]) * float(argv[2]) + float(argv[3])}')


