

import psycopg2

conn = psycopg2.connect(host = 'localhost',
                       database = 'ABOB',
                       port = '5433',
                       user = 'postgres',
                       password = '1234' )
cur = conn.cursor()

# cur.execute("SELECT username FROM ABOB32")
# usernames = [r[0] for r in cur.fetchall()]
# Found = False 
# while not Found:
cur.execute("SELECT username FROM ABOB32")
usernames = [r[0] for r in cur.fetchall()]
arr = usernames

username = input('')

def binary_search(arr, x):
    global coefizhent
    coefizhent = x
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            print(arr)
            return mid

    print("ba0b")
    return -1

result = binary_search(arr, username)
if result != -1:
    print(f"Имя пользователя {username} найдено в списке." , coefizhent)
else:
    print(f"Имя пользователя {username} не найдено в списке.")





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
