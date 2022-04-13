#todo: Посчитать сумму от 1 до 100

s100 = int(((1 + 100) / 2) * 100)
print("Сумма чисел от 1 до 100:",s100)

x = 0
y = 0
z = 0
for i in range(101):
    x = x + i
print("Сумма чисел от 1 до 100:",x)

while True:
    y = y + 1
    z = z + y
    if y == 100:
        break
print("Сумма числе от 1 до 100:",z)

