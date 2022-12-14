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
         ('Spread', 'Spread', 'Spread', 'распространять'),
         ('Bend', 'Bent', 'Bent', 'сгибать'),
         ('Bleed', 'Bled', 'Bled', 'кровоточить, истекать кровью'),
         ('Build', 'Built', 'Built', 'строить'),
         ('Deal', 'Dealt', 'Dealt', 'иметь дело с кем-либо'),
         ('Dream', 'Dreamt', 'Dreamt', 'видеть сны'),
         ('Feed', 'Fed', 'Fed', 'кормить'),
         ('Feel', 'Felt', 'Felt', 'чувствовать'),
         ('Find', 'Found', 'Found', 'находить'),
         ('Get', 'Got', 'Got', 'получать, становиться'),
         ('Have', 'Had', 'Had', 'иметь'),
         ('Hear', 'Heard', 'Heard', 'слышать'),
         ('Hold', 'Held', 'Held', 'удерживать'),
         ('Keep', 'Kept', 'Kept', 'держать'),
         ('Lay', 'Laid', 'Laid', 'класть, положить'),
         ('Lead', 'Led', 'Led', 'вести'),
         ('Leave', 'Left', 'Left', 'оставлять, уезжать'),
         ('Lend', 'Lent', 'Lent', 'одалживать, предоставлять'),
         ('lose', 'Lost', 'Lost', 'терять'),
         ('Make', 'Made', 'Made', 'делать'),
         ('Mean', 'Meant', 'Meant', 'означать'),
         ('Meet', 'Met', 'Met', 'встретить'),
         ('Pay', 'Paid', 'Paid', 'платить'),
         ('Read', 'Read', 'Read', 'читать'),
         ('Say', 'Said', 'Said', 'говорить'),
         ('Sell', 'Sold', 'Sold', 'продавать'),
         ('Send', 'Sent', 'Sent', 'посылать'),
         ('Shine', 'Shone', 'Shone', 'стрелять'),
         ('Sit', 'Sat', 'Sat', 'сидеть'),
         ('Sleep', 'Slept', 'Slept', 'спать'),
         ('Spend', 'Spent', 'Spent', 'проводить, тратить'),
         ('Stick', 'Stuck', 'Stuck', 'застревать, приклеиваться'),
         ('Strike', 'Struck', 'Struck', 'ударять, бить'),
         ('Tell', 'Told', 'Told', 'сказать, говорить'),
         ('Understand', 'Understood', 'Understood', 'понимать'),
         ('Win', 'Won', 'Won', 'выигрывать, побеждать'),
         ('Become', 'Became', 'Become', 'становиться'),
         ('Come', 'Came', 'Come', 'приходить'),
         ('Run', 'Ran', 'Run', 'бежать'),
         ('Drive', 'Drove', 'Driven', 'водить транспорт'),
         ('Ride', 'Rode', 'Ridden', 'ездить'),
         ('Rise', 'Rose', 'Risen', 'подниматься'),
         ('Write', 'Wrote', 'Written', 'писать'),
         ('Break', 'Broke', 'Broken', 'нарушать, ломать'),
         ('Choose', 'Chose', 'Chosen', 'выбирать'),
         ('Freeze', 'Froze', 'Frozen', 'замораживать'),
         ('Speak', 'Spoke', 'Spoken', 'говорить'),
         ('Steal', 'Stole', 'Stolen', 'украсть'),
         ('Tear', 'Tore', 'Torn', 'рвать'),
         ('Wake', 'Woke', 'Woken', 'просыпаться, будить'),
         ('Wear', 'Wore', 'Worn', 'носить(про одежду)'),
         ('Bite', 'Bit', 'Bitten', 'кусать'),
         ('Fall', 'Fell', 'Fallen', 'падать'),
         ('Forbid', 'Forbade', 'Forbidden', 'запрещать'),
         ('Forget', 'Forgot', 'Forgotten', 'забывать'),
         ('Get', 'Got', 'Gotten', 'получать'),
         ('Hide', 'Hid', 'Hidden', 'прятать'),
         ('Ride', 'Rode', 'Ridden', 'кататься, ехать'),
         ('Write', 'Wrote', 'Written', 'писать'),
         ('Blow', 'Blew', 'Blown', 'дуть'),
         ('Fly', 'Flew', 'Flown', 'летать'),
         ('Grow', 'Grew', 'Grown', 'расти'),
         ('Know', 'Knew', 'Known', 'знать'),
         ('Throw', 'Threw', 'Thrown', 'бросать'),
         ('Bring', 'Brought', 'Brought', 'приносить'),
         ('Buy', 'Bought', 'Bought', 'покупать'),
         ('Catch', 'Caught', 'Caught', 'ловить'),
         ('Fight', 'Fought', 'Fought', 'драться'),
         ('Seek', 'Sought', 'Sought', 'стремиться'),
         ('Teach', 'Taught', 'Taught', 'учить'),
         ('Think', 'Thought', 'Thought', 'думать'),
         ('Be', 'Was / were', 'Been', 'быть'),
         ('Do', 'Did', 'Done', 'делать'),
         ('Go', 'Went', 'Gone', 'идти')]


    cursor.executemany('''INSERT INTO Irregular_Verbs(Present, Past, Perfect, Translation) VALUES(?,?,?,?)''', words)
    cursor.execute('''SELECT * FROM Irregular_Verbs''')
    k = cursor.fetchall()
    print(k)
    #
    # cursor.execute('''DELETE FROM Irregular_Verbs''')