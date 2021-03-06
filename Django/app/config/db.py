import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

SQLITE = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db-eje.sqlite3')
    }
}

POSTGRESQL = {
    'default':{
        'ENGINE' : 'django.db.backends.postgresql_psycopg2', 
        'NAME' : 'db-eje', 
        'USER' : 'postgres', 
        'PASSWORD' : '12345', 
        'HOST' : 'localhost', 
        'PORT' : '5432' 
    }
}