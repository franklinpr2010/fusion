# fusion
Projeto Básico construído em python para uma empresa de serviços


Projeto criado no pycharm

Depois de criado o projeto no pycharm, instalar o django.

pip install django psycopg2-binary gunicorn dj-static django-stdimage

gunicorn - servidor do django
django-bootstrap4 -caso queira instalar o boostrap
pymysql - se quiser instalar o driver para acessar mysql
whitenoise - apresenta arquivos estáticos em produção.


pip freeze > requirements.txt

Criar o projeto 
django-admin startproject fusion .

Criar o aplicativo
django-admin startapp core

Para criar um usuário para ter acesso ao conteúdo administrativo do python
python manage.py createsuperuser

localhost:8000/admin


















