def user_words(txt):
    text = txt[0].upper()+txt[1:].lower()
    return text

string = input('Введите слова с маленькой буквы:')
for text in string.split(' '):
    print(f'{user_words(text)}', end=' ')
