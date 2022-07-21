'''Задана натуральная степень k. Сформировать случайным образом список коэффициентов
(значения от 0 до 100) многочлена и вывести на экран.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0'''
#bx**k + bx**(k-1) + bx**(k-2) = 0
import random
stepen = int(input("Введите старшую степень многочлена "))
equalString = " "
for i  in range(stepen,-1,-1):
        equalString +=str(random.randint(0,100))+'*' + 'x'+ '^' + str(i)+ " " + "+" + " "
finalString = equalString[:-6] + " " + "=" + " " + "0"
print(finalString)


