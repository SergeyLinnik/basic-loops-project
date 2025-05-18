# Задание 1: Сумма всех четных чисел от 1 до 100
sum_even = 0
for number in range(1, 101):
    if number % 2 == 0:
        sum_even += number
print(f"Сумма всех четных чисел от 1 до 100: {sum_even}")

# Задание 2: Список квадратов нечетных чисел от 1 до 10
squares_of_odds = [x**2 for x in range(1, 11) if x % 2 != 0]
print(f"Квадраты нечетных чисел от 1 до 10: {squares_of_odds}")

# Задание 3: Подсчет количества введенных положительных чисел
count = 0
print("Введите числа (введите отрицательное число для завершения):")

while True:
    num = int(input())
    if num < 0:
        break
    count += 1

print(f"Вы ввели {count} положительных чисел.")
