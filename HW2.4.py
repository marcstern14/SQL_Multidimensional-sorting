import sqlite3
import json

dbname = '../session_2.db'
fname = '../weather_newyork_dod.json'

fh = open(fname)
obj = json.load(fh)

conn = sqlite3.connect(dbname)

cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS weather_newyork')
cursor.execute('CREATE TABLE weather_newyork (date TEXT, mean_temp INT, precip FLOAT, events TEXT)')

query = "INSERT INTO weather_newyork (date, mean_temp, precip, events) VALUES (?, ?, ?, ?)"

for key in obj:
    val = obj[key]
    date = val['date']
    mean_temp = val['mean_temp']
    precip = val['precip']

    if precip == 'T':
        precip = None

    events = val['events']
    cursor.execute(query, (date, mean_temp, precip, events))


conn.commit()
