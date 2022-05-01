#todo: Числа в буквы
#Замените числа, написанные через пробел, на буквы. Не числа не изменять.

#Пример.
#Input	                            Output
#8 5 12 12 15	                    hello
#8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

alphabet = " abcdefghijklmnopqrstuvwxyz" # Алфавит, в индексе 0 записан пробел
txt = input("Введите сообщение для конвертации: ")
discription = ""
input_list = txt.split(" ") # В список записываю значения разделенные пробелом, удаляя пробелы

for letter in input_list: # Перебираю список
    if letter.isdigit(): # если значение в списке цифра, то
        n = int(letter) # то конвертирую в тип int
        discription = discription + alphabet[n] # Добавляю в строку значение из алфавита по индексу "n"
    else:
        discription = discription + letter # Если значение не цифра и не пробел, то записываю, как есть
print(discription)