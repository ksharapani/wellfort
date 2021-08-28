# wellfort
    manage.py makemigrations dashboard

    python manage.py migrate
    

#### Supervisor config
    supervisord -c /config-file.conf

    After any change
    sudo supervisorctl reread
    sudo supervisorctl update