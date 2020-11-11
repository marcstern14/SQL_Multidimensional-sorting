import csv
import sqlite3

fname = '../session_2.db'

newfname = 'revenue_from_db.csv'
wfh = open(newfname, 'w')
writer = csv.writer(wfh)

conn = sqlite3.connect(fname)

cursor = conn.cursor()

cursor.execute('SELECT * FROM revenue')
rev_col = cursor.fetchall()
lot = cursor.description

headers = writer.writerow([ col[0] for col in lot ])
rev_data = [ writer.writerow(col) for col in rev_col ]

wfh.close()
newfh = open(newfname)
newreader = newfh.read()
print(newreader)
