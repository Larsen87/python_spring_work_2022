# todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в
# процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов,
# дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07

# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

from datetime import datetime

last_time = datetime.now()

def logger(func): # функция записи в файл результатов декоратора(счётчика)
    log = func.__name__ + ", " + str(func.count) + ", " + last_time.strftime("%d.%m.%y %H:%M" + "\n")
    with open("debug.log", mode="a+", encoding="UTF-8") as f:
        f.write(log)
        f.close()


def counter(func):

    def wrapper(*args, **kwargs):
        wrapper.count += 1 # счётчик вызовов функции

        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__ # возвращает имя функции во врапер, это сделано для def logger, чтобы
                                     # в файл записывалось корретное наименование функции, а не "wrapper".
    wrapper.count = 0

    return wrapper



#блок декораторов для 3-х разных функций
@counter
def testing_def(a):
    a = a * 3
    return print(a)

@counter
def multiplication(x,y):
    res = x * y
    return res

@counter
def summ(x,y,z):
    res = x+y+z
    return res

#Блок вызова функций и их логирование в файл
testing_def(1)
testing_def(2)
testing_def(3)
logger(testing_def)

multiplication(2,3)
multiplication(34,3)
logger(multiplication)

summ(1,2,3)
summ(1,2,33)
summ(1,2,6)
summ(1,2,2)
logger(summ)
