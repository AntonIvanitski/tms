name = input('Введите имя:')
age = input('Введите ваш возраст:')

try:
 age = int(age)
except ValueError:
 print("Ошибка, повторите ввод")
def greetings():
    if int(age) <=0:
        print(f'Ошибка повторите ввод')
    elif 0 < age < 10:
        print(f'Привет, шкет {name}')
    elif 10 <= age <= 18:
        print(f'Как жизнь {name}?')
    elif 18 < age < 100:
        print(f'Чего желаете {name}?')
    else:
        print(f'{name}, вы лжёте - в наше время столько не живут...')
greetings()

