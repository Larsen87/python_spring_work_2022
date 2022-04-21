#todo: Модифицировать программу таким образом чтобы она выводила при повторном считывании стр. 5 приветствие "Hello"

f = open("text.txt", mode="r+", encoding="UTF-8")

f.write("Hello\n")
f.seek(0,0)
print(f.read())

f.close()

