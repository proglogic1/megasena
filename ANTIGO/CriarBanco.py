import sqlite3

conn = sqlite3.connect('loteria_new.db')

conn.execute('''CREATE TABLE megasena ( concurso text, date text,dezena1 text, dezena2 text, dezena3 text, dezena4 text, dezena5 text, dezena6 text)''')

conn.commit()

conn.close()