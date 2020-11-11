import sqlite3

fname = '../session_2.db'

conn = sqlite3.connect(fname)

cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS weather_newyork')
cursor.execute('CREATE TABLE weather_newyork (date TEXT, mean_temp INT, precip FLOAT, events TEXT)')

conn.commit()

