# https://www.youtube.com/watch?v=pd-0G0MigUA 
import sqlite3 

class Employee:
    def __init__(self, first, last, pay):
        self.last = last
        self.first = first
        self.pay = pay

    def get_email(self):
        return f'{self.first}.{self.last}@company.org'



conn = sqlite3.connect('test.db')

cur = conn.cursor() #once you have a cursor you can start executing sql commnands

# cur.execute("""CREATE TABLE employees (
#         first text,
#         last text,
#         pay integer
#         )""")

e = Employee('Miles', 'Davis', 40)

# cur.execute('DELETE FROM employees WHERE first == "Connor"')
cur.execute("INSERT INTO employees VALUES ('Connor', 'Hanwick', 20)")
# cur.execute(f"INSERT INTO employees VALUES ('{e.first}', '{e.last}', {e.pay})")

cur.execute('SELECT * FROM employees')

print(cur.fetchall())
# print(e.first)

conn.commit()

conn.close()

