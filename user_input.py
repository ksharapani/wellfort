from time import sleep
from datetime import datetime
import sqlite3

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
execute = con.execute('SELECT count(*) FROM message')
count = execute.fetchone()[0]
print(count)

while True:

    if button_2.wait_for_press():
        user = None
        message = None
        for row in con.execute('SELECT id FROM dashboard_user where pin_number=2'):
            user = row[0]
        for row in con.execute('SELECT id FROM dashboard_message where message_id=1'):
            message = row[0]

        con.execute('INSERT INTO dashboard_queue(created_at, clicked_user_id, display_message_id, displayed) '
                    'VALUES ("{}", {}, {}, 0);'.format(datetime.now(), user, message))

        con.commit()

    if button_2.wait_for_press():
        user = None
        message = None
        for row in con.execute('SELECT id FROM dashboard_user where pin_number=3'):
            user = row[0]
        for row in con.execute('SELECT id FROM dashboard_message where message_id=1'):
            message = row[0]

        con.execute('INSERT INTO dashboard_queue(created_at, clicked_user_id, display_message_id, displayed) '
                    'VALUES ("{}", {}, {}, 0);'.format(datetime.now(), user, message))

        con.commit()


    sleep(1)
