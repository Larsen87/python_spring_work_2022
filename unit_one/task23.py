#todo: Взлом шифра
#Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
#Попробуйте все возможные сдвиги и расшифруйте фразу.


txt = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
alphabet = "abcdefghijklmnopqrstuvwxyz"
discrypted = ""
n = 0

while n < 26: # Завожу цикл по числу букв в алфавите
    n += 1 # Перебираю добавляя к шагу + 1
    for letter in txt: # Смотрю текст по буквенно
        if letter in alphabet: # Если буква в списке алфавита
            position = alphabet.find(letter) # Определяю индекс буквы в алфавите
            new_position = position - n # Добавляю к индексу сдвиг по "n"
            discrypted = discrypted + alphabet[new_position] # записываю букву со сдвигом по "n"
        else:
            discrypted = discrypted + letter # Если символа нет в алфавите, то записываю без изменений
    print(discrypted) # Вывожу результат для сдвига "n"
    discrypted = "" # Отчищаю строку
