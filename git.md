Настройка
git config --global user.nam "ник"
git config --global user.email "email"

Просмотр настроек
git config --list

Создание репозитария 
git init

Далее создаём файл .gitignore

Индексация файла
git add

git rm -cached имя_файла // удаление индексации
git rm -f имя_файла // удаление из индекса и из проекта

Изменения
git status

git commit -m "комментарий"

git log // история коммитов

git remote add origin git@github.com:my_name/my_repo.git // связывание локального репозитария с гитхаб
Где my_name – имя пользователя на GitHub
    my_repo – название созданного репозитор

git remote get_url origin // проверка связывания
git remote remove origin // отвязывание

git push origin master // отправка изменений в удаленный репо origin ветки мастер
git push
git pull

git clone "ссылка на репозитарий"










