#  https://zetcode.com/db/sqlitepythontutorial/

import sqlite3 as lite
import sys

cone = None

try:
    con = lite.connect('test.db')

    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()[0]

    print(f'SQLite version: {data}'')

except lite.Error, e:

    print(f'Error {e.args[0]}')
    sys.exit(1)

finally:

    if con:
        print('got here')
        con.close()

