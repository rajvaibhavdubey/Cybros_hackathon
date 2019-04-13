import sqlite3

conn = sqlite3.connect('database.db')
print "Opened database successfully"

conn.execute('CREATE TABLE original ( id INTEGER PRIMARY KEY, sentences TEXT)')
conn.execute('CREATE TABLE output ( id INTEGER PRIMARY KEY, org_id INTEGER, sentences TEXT, score REAL, tsne STRING)')
conn.execute('CREATE TABLE translations(sentences TEXT, org_id INTEGER)')

conn.execute('INSERT INTO original (sentences) VALUES ( "org sent 1" )')
conn.execute('INSERT INTO original (sentences) VALUES ( "org sent 2" )')
conn.execute('INSERT INTO original (sentences) VALUES ( "org sent 3" )')
conn.execute('INSERT INTO original (sentences) VALUES ( "Heorg sent 1llo" )')
conn.execute('INSERT INTO original (sentences) VALUES ( "org sent 4" )')
conn.execute('INSERT INTO original (sentences) VALUES ( "org sent 5" )')
conn.execute('INSERT INTO original (sentences) VALUES ( "org sent 6" )')
conn.execute('INSERT INTO original (sentences) VALUES ( "org sent 7" )')
conn.commit()

print "Table created successfully"
conn.close()