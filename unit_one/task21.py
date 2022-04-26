#todo: Задан словарь, его значения необходимо внести по соответвющим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}


template = """ 
<!DOCTYPE HTML>
<html> <head>
  <title> ? </title>
  <meta charset=?>
 </head>
 <body onload="alert(?)">
 
  <p>?</p>

 </body>
</html>
"""
list_html = []
index = []
f = open("index.html", mode="w+", encoding="UTF-8")
f.writelines(template)

f = open("index.html", mode="r+t", encoding="UTF-8")

list_html = f.readlines() # Записываю в список файл по строчно

for key, val in page.items(): # Итерация словаря
        for i in list_html: # Итерируем строки из списка строк
                if key in i: # Если ключ есть в строке, то:
                        x = list_html.index(i) # Записал номер строки в которой есть ключ
                        i = i.replace("?", val) # Меняем в строке символ ? на значение из словаря
                        list_html[x] = i # Перезаписал строку в списке со значением val

f.seek(0,0)
f.writelines(list_html)

f.close()