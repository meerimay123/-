#Нахождение максимального элемента в списке:
#Программа находит и выводит самый большой элемент в списке.


list = [10, 131, 23, 45, 67,]
max_number = 0
for i in list:
    if i > max_number:
        max_number = i
print(max_number)