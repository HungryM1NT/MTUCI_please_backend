## Local Developing

1. Firstly, create and activate a new virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   
2. Install packages:
   ```bash
   pip install -r requirements.txt
   ```
   
3. Run project dependencies, migrations, fill the database with the fixture data etc.:
   ```bash
   python ./manage.py migrate
   python ./manage.py loaddata main_page/fixtures/persons.json
   python ./manage.py runserver 
   ```

