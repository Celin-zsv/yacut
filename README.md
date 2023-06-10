[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=30&pause=1000&color=F71329&multiline=true&width=435&lines=+yacut)](https://git.io/typing-svg)  
[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=20&pause=1000&color=1D39F7&multiline=true&width=435&lines=+yacut)](https://git.io/typing-svg)  
[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=15&duration=2000&pause=1000&color=1FBB30F6&multiline=true&width=435&lines=+yacut)](https://git.io/typing-svg)    
[![Typing SVG](https://img.shields.io/badge/yacut-sprint--21%20ver.2-red)](https://git.io/typing-svg)

### Проект: yacut. Спринт-21, ver.2, Зеленковский Сергей  
![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  
![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRK7h38B8oEy58nDXqK63UZH0I6dBW7ew_KjoPje6scjQ&s)
![](https://www.sqlalchemy.org/img/sqla_logo.png)

#### Содержание
1. Описание проекта
2. Установка
3. Запуск
***
### 1. *Описание проекта*


Parameter  | Value
-------------|:-------------
Наименование проекта  | yacut
Назначение проекта | YaCut — это сервис укорачивания ссылок (ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис). Доступны 2 интерфейса: web, api.
Tech Stack. Client. OS | Windows, Linux, MacOS
Tech Stack. Project |[Python](https://www.python.org/), [Flask](https://pypi.org/project/Flask/), [SQLAlchemy](https://pypi.org/project/SQLAlchemy/)
GitHub | https://github.com/Celin-zsv/yacut
Author | Sergei Zelenkovskii, svzelenkovskii@gmail.com  

### 2. *Установка*




2.1. клонировать репозиторий
```
cd dev
git clone git@github.com:Celin-zsv/yacut.git
```
2.2. создать и активировать виртуальное окружение:
```
  # Windows
python -m venv env
. env/Scripts/activate
  # Unix / MacOS
python3 -m venv env
source venv/bin/activate
```
2.3. обновить менеджер пакетов pip, установить зависимости requirements.txt:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
2.4. создать в корне файл .env + наполнить:
```
FLASK_APP=yacut
FLASK_ENV=<development или production>
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=<ваш_секретный_ключ>
```
### 3. *Запуск*

3.1. ввести команду: локально старт проекта
```
flask run
```
3.4. описание функционала:

URL  | Description.Short | Description.Full
-------------|:-------------|:-------------
http://127.0.0.1:5000/  | главная страница сервиса | 1)ввести URL в поле "Оригинальная длинная ссылка", 2)придумать и ввести значение в поле "Пользовательский короткий идентификатор" (16 сммволов max доступны для ввода: символы "a-z A-Z", цифры "0-9"), 3)Нажать кнопку "Создать ссылку", в результате: 3.1)ниже кнопки отобразится собщение "Ваша новая ссылка готова" + ссылка (в формате http://127.0.0.1:5000/ + введенный идентификатор), 3.2)перейти по созданной ссылке (переход на страницу оригинальной ссылки), 4)нажать (слева вверху) ссылку "Главная" (в результате: переход на главную страницу): 4.1)повторить ввод URL в поле "Оригинальная длинная ссылка" и нажать кнопку "Создать ссылку", 4.2)в результате: новая ссылка сгенерится автоматически (в формате http://127.0.0.1:5000/ + 6 случайных символов: a-z A-Z 0-9)
http://127.0.0.1:5000/api/id/   | эндпоинт POST | {  "url": "https://www.gazeta.ru/", "custom_id": "ga"}
http://localhost/api/id/short_id/   | эндпоинт GET | http://127.0.0.1:5000/api/id/ga
https://editor.swagger.io/   | спецификация API | https://github.com/Celin-zsv/yacut/blob/master/openapi.yml


@zsv
