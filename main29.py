
n = int(input("Введите число n (10 ≤ n ≤ 999): "))

if 10 <= n <= 999 and (n // 10) % 10 != 0:
    tens = n // 10  
    units = n % 10 

    
    second_digit = tens
    first_digit = (n // 100) if (n >= 100) else (tens // 10)
    
    
    x = first_digit * 100 + second_digit * 10 + units

    print(f"Найденное трехзначное число x: {x}")
else:
    print("Число не соответствует заданным условиям.")

