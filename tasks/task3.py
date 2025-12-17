# tasks/task1.py



def solve():
# Ниже пишите решение задачии(Обязательно поставьте четыре пробела после функции Solve())
    # Запрос веса и роста
    weight = float(input())
    height = float(input())
    bmi = weight / (height ** 2)
    print(f"Индекс массы тела (ИМТ): {bmi}")  # Без :.2f
   

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()