#todo: Числа в буквы
#Замените числа, написанные через пробел, на буквы. Не числа не изменять.

#Пример.
#Input	                            Output
#8 5 12 12 15	                    hello
#8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

alphabet = " abcdefghijklmnopqrstuvwxyz"
txt = input("Введите сообщение для конвертации: ")
discription = ""
input_list = txt.split(" ")

for letter in input_list:
    if letter.isdigit():
        n = int(letter)
        discription = discription + alphabet[n]
    else:
        discription = discription + letter
print(discription)