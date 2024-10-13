**Платформа торговой сети по продаже электроники**
Проект представляет собой API платформы торговой сети по продаже электроники.

**Технологии**
Python 3.8+
Django 3+
DRF 3.10+
PostgresQL (БД для хранения данных)

**Запуск проекта:**

1) Клонируйте репозиторий https://github.com/Denis-Ki/Electtronics-sales.git на свой компьютер.
2) Перейдите в корневую директорию проекта, создайте в ней и активируйте виртуальное окружение: python -m venv venv
venv\Scripts\activate.bat
3) Установите зависимости:
pip install -r requirements.txt
4) Создайте .env файл в корневой директории проекта и заполните переменные из файла .env.sample.
5) Выполните миграции:
python manage.py migrate
6) Создайте суперпользователя:
python manage.py csu
   (email: admin_1@example.com, password: admin)
7) В папке fixtures есть фикстуры для заполнения базы данных тестовыми данными
8) Запустите проект:
python manage.py runserver

**Документация по  API доступна по ссылкам:**
http://localhost:8000/swagger/ - Swagger 
http://localhost:8000/redoc/ - ReDoc

**Для запуска проекта через Docker необходимо выполнить командs:**

1) Сборка образа и запуск в фоне после успешной сборки
docker-compose up -d --build
2) Для остановки контейнеров и удаления созданных ресурсов выполните команду:
docker-compose down

**Автор проекта:**
https://github.com/Denis-Ki