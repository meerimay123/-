#Поиск отрицательного числа в списке:
#Программа использует цикл while, чтобы проверить, есть ли в списке отрицательное число. Если находится отрицательное число,
#программа выводит сообщение о его наличии, в противном случае выводится сообщение об его отсутствии.


number_list = [12, 34, 56, 3, -45]
number1 = len(list)-1
i = 0
while True:
    if list[i] < 0:
        print("est otricatelnoe chislo")
        break
    elif i == number1:
        print("net otricatelnogo chisla")
        break

    i = i + 1

