import sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    line = line.strip()
    if not line.startswith('From:') : continue
    y = re.findall('^From.*?@([a-z0-9.]*)', line)
    if len(y) == 0:
        continue
    #pieces = line.split()
    #email = pieces[1]
    #lst = email.split("@")
    #domain = lst[1]
    #print domain
    for i in range(len(y)):
        domain = y[i]
        domain = str(domain)
        domain = domain.strip()
        print domain
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain, ))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, 1 )''', (domain, ) )
        else : 
            cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
                (domain, ))
    # This statement commits outstanding changes to disk each 
    # time through the loop - the program can be made faster 
    # by moving the commit so it runs only after the loop completes
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print
print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()

