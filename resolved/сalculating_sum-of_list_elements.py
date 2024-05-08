#Вычисление суммы элементов списка:
#Программа вычисляет и выводит сумму всех элементов списка, который вводит пользователь.

my_list = [18, 23, 12, 25, 89]
total_sum = 0
for item in my_list:
    total_sum = total_sum + item
print(total_sum)
