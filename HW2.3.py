import sqlite3

dbname = '../session_2.db'
fname = '../weather_newyork.csv'

fh = open(fname)
headers = next(fh)

conn = sqlite3.connect(dbname)

cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS weather_newyork')
cursor.execute('CREATE TABLE weather_newyork (date TEXT, mean_temp INT, precip FLOAT, events TEXT)')

query = "INSERT INTO weather_newyork (date, mean_temp, precip, events) VALUES (?, ?, ?, ?)"

for row in fh:
    line = row.split(',')
    date = line[0]
    mean_temp = line[1]
    precip = line[-4]

    if precip == 'T':
        precip = None

    events = line [-2]

    cursor.execute(query, (date, mean_temp, precip, events))

conn.commit()
