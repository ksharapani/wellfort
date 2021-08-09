

from time import sleep
import sqlite3


from gpiozero import Button
button_2 = Button(2)

con = sqlite3.connect('db.sqlite3')


while True:
    if button_2.wait_for_press():
        users = con.execute('SELECT id FROM dashboard_user where pin_number=2')
        messages = con.execute('SELECT id FROM dashboard_message where message_id=1')

        # messages = con.execute('INSERT INTO dashboard_queue(clicked_user, display_message, ) VALUES ({}, {]);'.
        #                        format(users[0]))


            # print(row[0])
        print('clicked')

    sleep(1)

