def user_data(name,surname,year, city, mail, phone):
    result=(name,surname,year, city, mail, phone)
    return result
user_name=input('Имя:')
user_surname=input('Фамилия:')
user_year=input('Год рождения:')
user_city=input('Город:')
user_mail=input('Эл.почта:')
user_phone=input('Телефон:')

user_data_1= user_data(name=user_name, surname=user_surname, year=user_year, city =user_city, mail=user_mail, phone=user_phone)
print(user_data_1)
