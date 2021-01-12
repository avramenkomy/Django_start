
Развертывание проекта на локальном устройстве
В командной строке набираем: 
1. git clone https://github.com/YuriyShashurin/SocialAccounts_HW.git
2. Переходим в папку проекта: cd django_auth
3. Создаем командное окружение и запускаем его
   -python -m venv C:/YourFolder/django-auth/env
   - Launch: C:/YourFolder/django-auth> env\Scripts\activate.bat
4. Устанавливаем модули совместимостей pip install -r requirements.txt
5. запускаем проект python manage.py runserver

Проходим по адресу http://127.0.0.1:8000, нажимем регистрация, заводим логин и пароль, после этого заводим профиль и сохраняем внесенные данные.
После этого появится информация по профилю. Профиль - экземлпляр объекта SocialAccounts (allauth)

Отображение пока кустарное.
