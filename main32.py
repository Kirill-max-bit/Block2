target_number = 654


last_digit = target_number // 100        
first_digit = (target_number // 10) % 10  
second_digit = target_number % 10         


for x in range(100, 1000):
    hundreds = x // 100          
    tens = (x // 10) % 10       
    units = x % 10               

    if units == last_digit and (tens * 10 + hundreds) == (first_digit * 10 + second_digit):
        print(f"Найденное трехзначное число x: {x}")
        break

