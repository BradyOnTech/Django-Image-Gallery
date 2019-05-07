# BoT-django-skeleton
A Django skeleton to make setting up a new project quicker

Steps to get up and running:
 - Clone repo into local folder (git clone https://github.com/BradyOnTech/BoT-django-skeleton.git)
 - Open command line and do the following:
     - change directory into the "src" folder
     - create virtual environment and start it
     - pip install -r requirements.txt
  - Change name of folder from "BoT-django-skeleton" to whatever you would like
  - Change name of project from "project" in the following areas to whatever you would like the project to be called:
  
     settings.py:
     - ROOT_URLCONF = '<strong>project</strong>.urls'
     - WSGI_APPLICATION = '<strong>project</strong>.wsgi.application'
     
     wsgi.py
     - os.environ.setdefault('DJANGO_SETTINGS_MODULE', '<strong>project</strong>.settings')
     
     manage.py
     - os.environ.setdefault('DJANGO_SETTINGS_MODULE', '<strong>project</strong>.settings')
     
 - Update .env file in the "src" folder directory
   - Change secret key value by generating a new one with the following:
   - enter "python" in command line to enter python terminal
   - enter "from django.core.management.utils import get_random_secret_key"
   - enter "get_random_secret_key()"
   - copy given secret key into .env file without the leading and following quotes
