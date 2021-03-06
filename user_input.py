import sqlite3
import random
from time import sleep
from datetime import datetime

from gpiozero import Button
button_2 = Button(2)
button_3 = Button(3)
button_4 = Button(4)
button_5 = Button(5)
button_6 = Button(6)
button_7 = Button(7)
button_8 = Button(8)
button_9 = Button(9)
button_10 = Button(10)
button_11 = Button(11)
button_12 = Button(12)


con = sqlite3.connect('db.sqlite3')
execute = con.execute('SELECT * FROM dashboard_message')
messages = execute.fetchall()
count = len(messages)

while True:
    random_number = random.randint(1, count)
    if button_2.is_pressed:
        print('press 2')
        execute = con.execute('SELECT id FROM dashboard_user where pin_number=2')
        user = execute.fetchone()[0]

        con.execute('INSERT INTO dashboard_queue(created_at, clicked_user_id, display_message_id, displayed) '
                    'VALUES ("{}", {}, {}, 0);'.format(datetime.now(), user, messages[random_number-1][0]))

        con.commit()

    if button_3.is_pressed:
        print('press 3')
        execute = con.execute('SELECT id FROM dashboard_user where pin_number=3')
        user = execute.fetchone()[0]

        con.execute('INSERT INTO dashboard_queue(created_at, clicked_user_id, display_message_id, displayed) '
                    'VALUES ("{}", {}, {}, 0);'.format(datetime.now(), user, messages[random_number-1][0]))

        con.commit()

    sleep(0.1)
