

import psycopg2

conn = psycopg2.connect(host = 'localhost',
                       database = 'ABOB',
                       port = '5433',
                       user = 'postgres',
                       password = '1234' )
cur = conn.cursor()

cur.execute("SELECT username FROM ABOB32")
usernames = [r[0] for r in cur.fetchall()]
Found = False 
while not Found:
    username = input('Login:')
    if username in usernames:
        print('Welcome')
        Found=True
    else:
        print('Enter valid login please')

conn.commit()
cur.close()
conn.close()

# import turtle

# t = turtle.Turtle()

# # рисуем лицо
# t.circle(100)

# # рисуем левый глаз
# t.penup()
# t.goto(-35, 120)
# t.pendown()
# t.dot(25)

# # рисуем правый глаз
# t.penup()
# t.goto(35, 120)
# t.pendown()
# t.dot(25)

# # улыбка
# t.penup()
# t.goto(-50, 60)
# t.pendown()
# t.setheading(-60)
# t.circle(50, 120)

# turtle.done()
