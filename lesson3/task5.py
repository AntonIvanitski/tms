import random
number = random.randint(1,10)
def guessing_game(input_):

    if number == input_:
        print('Угадал!')
    elif input_ > number:
        print('Много!')
    else:
        print('Мало!')
while True:
    guessing_game(int(input('Введите число:')))
#guessing_game(int(input('Введите число:')))
