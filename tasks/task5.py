# tasks/task1.py



def solve():
# Ниже пишите решение задачии(Обязательно поставьте четыре пробела после функции Solve())
    # Запрос чисел через пробел
    numbers_str = input("Введите числа: ")
    # Преобразование строки в список чисел
    numbers = list(map(int, numbers_str.split()))
    # Вычисление квадратов чисел
    squares = [num ** 2 for num in numbers]
    # Вывод результата
    result_str = ' '.join(map(str, squares))
    print(f"Результат: {result_str}")

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()