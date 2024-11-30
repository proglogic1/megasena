import sqlite3

conn = sqlite3.connect('loteria_new.db') 

cursor  = conn.execute("""SELECT * FROM megasena WHERE dezena1 = '21' and dezena2 ='24' and dezena3 ='33' and dezena4 = '41' and dezena5 ='48' and dezena6 ='56'""")
valores = cursor.fetchall()

for valor in valores:
    print(valor)
    
conn.close()