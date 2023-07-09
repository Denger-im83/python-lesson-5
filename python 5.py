# Создайте список из случайных чисел. Найдите номер его последнего локального максимума.
# Локальный максимум - элемент, который больше любого из своей соседей.

# import random
# n = int(input('Введите количество элементов: '))
# list = [random.randint(-50, 50) for item in range(n)]
# print(list)
# local_max = 0
# for i in range(1, len(list) - 1):
#      if list[i] > list[i - 1] and list[i] > list[i + 1]:
#          local_max = list[i]
# print(local_max)
# print(i)

# Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.
# import random 
# my_list = [random.randint(1,10) for i in range(20)] 
# print(my_list) 
# max_count = 0 
# for i in set(my_list): 
#     if my_list.count(i) > max_count: 
#         max_count = my_list.count(i) 
# print("Максимальное количество одинаковых элементов:", max_count) 

# Создайте список из случайных чисел. Найдите второй максимум.

# import random
# n = int(input('Введите количество элементов: '))
# list = [random.randint(-50, 50) for item in range(n)]
# print(list)
# list.sort()
# print(list[-2])
# Создайте список из случайных чисел. Найдите количество различных элементов в нем.
# array = input("Введите список через пробел").split()
# count = 0
# unique_array = []
# for x in array:
#     if x not in unique_array:
#         count += 1
#         unique_array.append(x)
# print(len(unique_array))


