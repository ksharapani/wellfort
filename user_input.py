from time import sleep
from datetime import datetime
import sqlite3


from gpiozero import Button
button_2 = Button(2)

con = sqlite3.connect('db.sqlite3')


while True:
    if button_2.wait_for_press():
        user = None
        message = None
        for row in con.execute('SELECT id FROM dashboard_user where pin_number=2'):
            user = row[0]
        for row in con.execute('SELECT id FROM dashboard_message where message_id=1'):
            message = row[0]

        print('INSERT INTO dashboard_queue(created_at, clicked_user_id, display_message_id, displayed) VALUES '
              '("{}", {}, {}, 0);'.format(datetime.now(), user, message))
        messages = con.execute('INSERT INTO dashboard_queue(created_at, clicked_user_id, display_message_id, '
                               'displayed) VALUES ("{}", {}, {}, 0);'.format(datetime.now(), user, message))
        print('clicked')

    sleep(1)

