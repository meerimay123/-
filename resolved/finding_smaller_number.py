#Нахождение наименьшего числа:
#Программа принимает три целых числа от пользователя и выводит значение наименьшего из них.


number1 = int(input("Введите число1"))
number2 = int(input("Введите число2"))
number3 = int(input("Введите число3"))
if number1 < number2 < number3:
    print(number1)
elif number1 < number3 < number2:
    print(number1)
elif number2 < number1 < number3:
    print(number2)
elif number2 < number3 < number1:
    print(number2)
elif number3 < number1 < number2:
    print(number3)
elif number3 < number2 < number1:
    print(number3)
else:
    print("vawi chisla ravny")