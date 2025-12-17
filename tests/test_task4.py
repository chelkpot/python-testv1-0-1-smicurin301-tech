import pytest
from unittest.mock import patch
from io import StringIO
import os

# Проверяем, существует ли файл tasks/task4.py. Если нет, пропускаем тест.
@pytest.mark.skipif(not os.path.exists("tasks/task4.py"), reason="File tasks/task4.py does not exist")
def test_task4_celsius_to_fahrenheit(capsys):
    # Импортируем решение только если файл существует
    from tasks.task4 import solve
    with patch('builtins.input', side_effect=['20']): # Имитируем ввод 20 градусов Цельсия
        solve()
        captured = capsys.readouterr()
        # Проверяем, что вывод содержит ожидаемую температуру в Фаренгейтах
        assert "68.0" in captured.out
        # Задание 4. Перевод температуры
    C = float(input("Введите температуру в градусах Цельсия: "))
    F = (9/5) * C + 32
    print(f"Температура в градусах Фаренгейта: {F}")