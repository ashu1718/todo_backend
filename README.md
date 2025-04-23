Built with:
Django REST Framework for backend (deployed on Railway)

railway deployed link- https://todobackend-production-bd98.up.railway.app/

reproduce below steps to run it locally 
1. git clone https://github.com/ashu1718/todo_backend.git
2. cd todo_backend
3. python -m venv .venv  // create virtual env
4. .venv/Scripts/Activate  // activate virtual venv
5. pip install -r requirements.txt
6. python manage.py makemigrations
7. python manage.py migrate
8. python manage.py runserver
9. add your allowed frontend domains
      ALLOWED_HOSTS = ['localhost', '127.0.0.1']   // add your frontend domains

backend should be running
      
