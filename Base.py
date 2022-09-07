import sqlite3

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        user_login VARCHAR(20),
        user_password VARCHAR(20),
        user_email VARCHAR
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS goals(
            user_login VARCHAR(20),
            goal VARCHAR(20),
            goal_task VARCHAR(30),
            data_start DATE,
            data_end DATE,
            FOREIGN KEY(user_login) REFERENCES users(user_login)
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS mativation(
            user_login VARCHAR(20),
            goal VARCHAR(20),
            description VARCHAR(150),
            FOREIGN KEY(user_login) REFERENCES users(user_login)
            FOREIGN KEY(goal) REFERENCES goals(goal)
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS habits(
            user_login VARCHAR(20),
            habit VARCHAR(20),
            data_start DATE,
            FOREIGN KEY(user_login) REFERENCES users(user_login)
    )""")

    #============================================================================
    # lern English
    