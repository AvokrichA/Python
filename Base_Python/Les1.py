# num=int(input('Введите число:'))
# sum=num+2
# print(sum)

# Задача 2.
# Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.

# while True:
#   num=int(input('Введите число'))
#   if num>0 and num<10:
#       print(num**2)
#       break
#   else:
#     print('Введите число от 0 до 10')

# Задача 3
# Создайте программу “Медицинская анкета”, где вы запросите у пользователя следующие данные: имя, фамилия, возраст и вес.
# Выведите результат согласно которому:
# Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии.
# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!
#
# name=input('Введите имя:')
# syrname=input('Введите фамилию:')
# age=int(input('Введите возраст:'))
# weight=int(input('Введите вес:'))
#
# if age<=30 and (weight<=120 and weight>=50):
#     print(name, syrname, age,'год', weight, 'кг','-Хорошее состояние')
# elif age>30 and age<=40 and (weight<50 or weight>120):
#     print(name, syrname, age,'год', weight, 'кг' '-Займитесь собой')
# elif age>40 and (weight<50 or weight>120):
#     print(name, syrname, age,'год', weight, 'кг', '-Обратитесь к врачу')
#
# else: "Все же сходите ко врачу"   (Примечание: можно написать это строчку, но по заданию она не требуется)


