#ЗАДАНИЕ 1
#user_name = input ("Представьтесь")
#print(user_name)
#phone_user = input ("Введите номер телефона")
#print(phone_user)
#print(f"user_name, спасибо, что обратились к нам")
#str1= f"Здравствуйте, {user_name}! Спасибо за обращние в нашу службу! Наш специалист свяжется с вами по телефону {phone_user} завтра с 9-00 до 10-00"
#print(str1)

# ЗАДАНИЕ 2
#sec = int(input("Сколько секунд?"))
#hour = sec//3600
#sec = sec%3600
#min = sec//60
#sec = sec%60
#print(f"{hour}:{min}:{sec}")

#ЗАДАНИЕ 3
#n = str (input ("Введите число"))
#nn=int(n+n)
#nnn=int(n+n+n)
#m=int(n)+nn+nnn
#print(m)

#ЗАДАНИЕ 4
#user_namber = int(input("Напиши целое положительное число:"))
#n=user_namber%10
#user_namber = user_namber//10
#while user_namber>0:
#    if user_namber % 10 > n:
#        n=user_namber%10
#    user_namber=user_namber//10
#print(n)

#ЗАДАНИЕ 5
#revenue=int(input("Сумма выручки за год:"))
#costs=int(input("Сумма издержек:"))
#profit=revenue-costs
#profitability=profit/revenue
#if profit < 0:
#   print("Вы ничего не заработали в этом году!")
#      # elif profit = 0:
#   #print("Без убытков, но и без прибыли")
#elif profit>0:
#   print("Отлично поработали! Ваша прибыль в этом году:", profit, ". Рентабельность:", profitability)
#   people=int(input("Укажите число сотрудников в вашей фирме:"))
#   profit1=profit/people
#   print(' Прибыль фирмы в расчете на одного сотрудника составляет:',profit1)

#ЗАДАНИЕ 6
a = 2
b = 3
i = 1
while a < b:
    a *= 1.1
    i += 1
print(i)






