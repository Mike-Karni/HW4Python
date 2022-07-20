# Initialize denominator
k = 1
# Initialize sum
s = 0
for i in range(1000000):
    # even index elements are positive
    if i % 2 == 0:
        s += 4/k
    else:
        # odd index elements are negative
        s -= 4/k
    # denominator is odd
    k += 2
print(s)
d = int(input("Введите точность числа пи "))
sString = str(s)
print(sString[:d+2])
list = []
for numbers in sString:
  list.append(numbers)
print(list)
for i in range(d+2):
  print(list[i],end = "")