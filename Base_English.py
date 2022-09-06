import sqlite3

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Irregular_Verbs(
           ID INTEGER PRIMARY KEY AUTOINCREMENT,
           Present TEXT(20),
           Past TEXT(20),
           Perfect TEXT(20),
           Translation TEXT(20)
           )''')

    words = [('Bet', 'Bet', 'Bet', 'держать пари, делать ставку'),
         ('Burst', 'Burst', 'Burst', 'взорваться'),
         ('Cast', 'Cast', 'Cast', 'бросать, лить'),
         ('Cost', 'Cost', 'Cost', 'стоить'),
         ('Cut', 'Cut', 'Cut', 'резать'),
         ('Fit', 'Fit', 'Fit', 'примерять'),
         ('Hit', 'Hit', 'Hit', 'ударять'),
         ('Hurt', 'Hurt', 'Hurt', 'причинять боль'),
         ('Let', 'Let', 'Let', 'давать, позволять'),
         ('Put', 'Put', 'Put', 'класть'),
         ('Quit', 'Quit', 'Quit', 'покидать'),
         ('Set', 'Set', 'Set', 'устанавливать, задавать'),
         ('Shed', 'Shed', 'Shed', 'пролить'),
         ('Shut', 'Shut', 'Shut', 'закрывать'),
         ('Split', 'Split', 'Split', 'раскалывать, расщеплять'),
         ('Spread', 'Spread', 'Spread', 'распространять')]

    cursor.executemany('''INSERT INTO Irregular_Verbs(Present, Past, Perfect, Translation) VALUES(?,?,?,?)''', words)
    cursor.execute('''SELECT * FROM Irregular_Verbs''')
    k = cursor.fetchall()
    print(k)
    #
    # cursor.execute('''DELETE FROM Irregular_Verbs''')