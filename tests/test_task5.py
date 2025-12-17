# Задание 5. Квадраты чисел (map)
numbers = input("Введите числа: ")
num_list = list(map(int, numbers.split()))
squares = [num ** 2 for num in num_list]
print("Результат:", *squares)