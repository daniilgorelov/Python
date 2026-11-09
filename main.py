import os
import time

enabled = True
os.system('cls')

while enabled:
    os.system('cls')
    print('Простой калькулятор.')
    print("1. Сложить два числа.")
    print("2. Вычесть два числа.")
    print("3. Умножить два числа.")
    print("4. Разделить число а на в.")
    print("5. Перевод числа из системы (до 10) в десятичную.")
    print("6. Выход.")

    n = int(input("Введите номер действия: "))

    # Исправлена проверка диапазона пунктов меню (было: 0 > n > 5)
    if 1 <= n <= 5:
        if n == 5:
            # Логика из N_Less10_to_dec.py
            radix = int(input("Введите основание системы (до 10): "))
            if radix < 2 or radix > 9:
                print("Некорректное основание, повторите ввод.")
            else:
                a_num = input(f"Введите число в {radix}-й системе: ")
                a_r = a_num[::-1]
                l_a = len(a_num)
                summ = 0
                for i in range(l_a):
                    summ += int(a_r[i]) * radix**i
                print(f"Результат: число {a_num} в {radix}-й системе = {summ} в десятичной.")
            input("Нажмите Enter чтобы продолжить")
        else:
            a = int(input("Введите число а: "))
            b = int(input("Введите число b: "))
            
            if n == 1:
                print("Результат:", a + b)
                input("Нажмите Enter чтобы продолжить")
            elif n == 2:
                print("Результат:", a - b)
                input("Нажмите Enter чтобы продолжить")
            elif n == 3:
                print("Результат:", a * b)
                input("Нажмите Enter чтобы продолжить")
            elif n == 4:
                if b == 0:
                    print("Ошибка: деление на ноль!")
                else:
                    print("Результат:", a / b)
                input("Нажмите Enter чтобы продолжить")
                
    elif n == 6:
        print('До скорых встреч!')
        enabled = False
    else:
        print('Повторите ввод!', end=' ')
        input("Нажмите Enter чтобы продолжить")