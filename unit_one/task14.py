#todo: Дан массив размера N. Найти индексы двух ближайших чисел из этого массива.

#Пример:
#mass = [1,2,17,16,30,51,2,70,3,2]

#Для числа 2 индексы двух ближайших чисел: 6 и 9

#Пример:
#mass = [1,2,17,54,30,89,2,1,6,2]
#Для числа 1 индексы двух ближайших чисел: 0 и 7
#Для числа 2 индексы двух ближайших чисел: 6 и 9

mass = []
n = int(input("Введите длину массива:")) #Задаем длину списка
int_ = int(input("Введите число для индексации в массиве:"))
count = 1
ai = []
aj = []
a3 = []

while True: #Цикл для наполнения списка элементами
    mass.append(int(input("Введите целочисленное: ")))
    print("Осталось ввести ещё", n - count, "чисел.")
    count += 1
    if count == n+1:
        break

r = mass.count(int_) #число совпадений

for i in range(len(mass)): #Цикл для подбора совпадающих значений в массиве
    for j in range(i):
        if mass[i] == mass[j] and int_ == mass[i]:
            ai.append(i)
            aj.append(j)

#вычислить разницу по модулю список ai aj, может быть использовать сортивроку и клонирование?
#ввести третий список и через него вычислить разницу?
#как убрать дублирующие значения из списка?

print("""
Для, списка:""",mass, """
Индексы числа""", int_, """ равны -""")
print(aj)
print(ai)



