# wellfort

    pip install -r requirements.txt

    python manage.py makemigrations dashboard
    python manage.py migrate

    python manage.py runserver
    

#### Supervisor config
    supervisord -c /config-file.conf

    After any change
    sudo supervisorctl reread
    sudo supervisorctl update