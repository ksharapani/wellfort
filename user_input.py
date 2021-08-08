from time import sleep
import sqlite3

from gpiozero import Button
button_2 = Button(2)

con = sqlite3.connect('db.sqlite3.db')
cur = con.cursor()


while True:
    if button_2.wait_for_press():
        for row in cur.execute('SELECT * FROM user where pin_number=1'):
            print(row)
        print('clicked')

    sleep(1)
