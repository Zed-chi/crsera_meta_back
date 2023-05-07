# Capstone project from meta-back course

### Requirements:
- python 3.8+
- mysql

### Install:
- `pip install -r requirements.txt`
- add some table, users to mysql
- add values to `.env` file (see keys in `.env_example`)

### Exec
- `python manage.py migrate`
- `python manage.py runserver`


### Endpoints to Test:

Registration[POST] - http://127.0.0.1:8000/api/auth/users/

User Details[GET] - http://127.0.0.1:8000/api/auth/users/me/

Login/TokenGet[POST] - http://127.0.0.1:8000/api/auth/token/login/

Logout[POST]- http://127.0.0.1:8000/api/auth/token/logout/

Bookings[POST] - http://127.0.0.1:8000/api/bookings

Menu List[GET/POST] - http://127.0.0.1:8000/api/menu/

MenuItem[GET] - http://127.0.0.1:8000/api/menu/<int:pk>"
