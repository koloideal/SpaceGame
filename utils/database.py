import sqlite3
import socket

name = socket.gethostname().strip()


def push_score(score):

    connection = sqlite3.connect('DataBase/highscore.db')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS players (name, score INTEGER) ''')
    connection.commit()

    cursor.execute('SELECT name FROM players WHERE name="%s"' % name)
    resu = cursor.fetchone()

    if resu is None:

        cursor.execute('INSERT INTO players (name, score) VALUES ("%s", "%s")' % (name, score))
        connection.commit()
        connection.close()

    else:

        cursor.execute('UPDATE players SET score="%s" WHERE name="%s"' % (score, name))
        connection.commit()
        connection.close()


def pull_score():

    connection = sqlite3.connect('DataBase/highscore.db')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS players (name PRIMARY KEY, score INTEGER) ''')
    connection.commit()
    cursor.execute('SELECT score FROM players WHERE name="%s"' % name)
    res = cursor.fetchone()

    if res is None:

        cursor.execute('INSERT INTO players (name, score) VALUES ("%s", "%s")' % (name, 0))
        connection.commit()
        connection.close()

        return (0,)

    else:

        connection.commit()
        connection.close()

        return res


