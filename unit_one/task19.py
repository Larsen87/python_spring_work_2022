"""#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
– id - номер по порядку (от 1 до 10);
– текст из списка algoritm"""

algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]

x = open("algoritm.csv", mode="w+", encoding="UTF-8")

for i in range(1,len(algoritm)):
    x.writelines(str(i) + "," + algoritm[i] + "\n")

x.seek(0,0)
print(x.read())

x.close()
