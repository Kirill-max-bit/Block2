# Ищем число x
for x in range(100, 1000):  # Перебор всех трехзначных чисел
    str_x = str(x)
    second_digit = str_x[1]  # Вторая цифра
    new_number = int(second_digit + str_x[0] + str_x[2])  # Зачеркнули вторую цифру и приписали её слева
    if new_number == 546:  # Проверяем условие
        print(f"Найдено число x: {x}")
        break  # Прерываем цикл, так как нужное x найдено

