#Угадай рандомное число:
#Программа генерирует случайное число и предлагает пользователю угадать его. При каждой попытке программа подсказывает,
#больше или меньше загаданное число введенного пользователем числа.

from random import randint
random_number = randint(1, 101)
while True:
    num = int(input(" ugadayte chislo ot 1 do 100"))
    if num == random_number:

        print("Vy ugadali moe chislo")
        break
    elif num < random_number:
        print("vawe chislo menwe chem moe")
    elif num > random_number:
        print("vawe chislo bolwe chem moe")
