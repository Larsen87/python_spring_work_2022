#todo: Написать функцию logger() которая принимает в качестве аргумента текст который дописывается
# в файл error.log Новое сообщение должно распологаться на новой строчки.

def logger(x):

    f = open("error.log", mode="a", encoding="utf8")

    f.write(x+"\n")

    f.close()

y = "test"

logger(y)
logger(y)


