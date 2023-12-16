## Запуск проекта

1. Создание и активирование виртуального окружения:
   ```bash
   py -m venv venv
   venv\Scripts\activate
   ```
   
2. Установка необходимых библиотек:
   ```bash
   pip install -r requirements.txt
   ```
   
3. Заполнение базы данных и запуск сервера:
   ```bash
   py mtuci_please_backend/manage.py migrate
   py mtuci_please_backend/manage.py loaddata mtuci_please_backend/persons.json
   py mtuci_please_backend/manage.py runserver 
   ```

