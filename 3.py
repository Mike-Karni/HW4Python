#Задайте натуральное число N. Напишите программу, которая составит список простых
# делителей числа N.
#(1 - составное число)

'''
a = int(input("Введите число: "))
spisok = []

for i in range(2, a // 2+1):
    if (a % i == 0):
        spisok.append(i)
print(f"Cписок делилитей числа {a}  = {spisok}  {a}")
'''

'''
n = int(input("n= "))
lst = []
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            # если делитель найден, число не простое.
            print(i, end= " ")
    else:
        lst.append(i)
print(lst)
'''

number = int(input("Введите целое число: "))
print(f"Простые делители числа {number}:", end = " ")
for i in range(number - 1, 1, -1):
    is_simple = 0 # Счётчик
    if (number % i == 0):
        for j in range(i - 1, 1, -1):
            if (i % j == 0):
                is_simple = is_simple + 1 # Увеличиваем, если находим делитель
        if (is_simple == 0): # Если делителей не было найдено, выводим
            print(i, end = " ")