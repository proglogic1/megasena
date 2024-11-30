import sqlite3


def inserirbanco(megasena, concurso, data, dezenas1, dezenas2, dezenas9, dezenas4, dezenas5, dezenas6):
    conn = sqlite3.connect('loteria_new.db')
    
    conn.execute("INSERT INTO {} VALUES (?,?,?,?,?,?,?,?)".format(megasena), 
                 (data,concurso, dezenas1, dezenas2, dezenas3, dezenas4, dezenas5, dezenas6))
    conn.commit()
    conn.close()  