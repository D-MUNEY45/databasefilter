# Download the databse file of database.db.  The file contains a table with 50 country names with their area in square km in population.
#Use Python to print out those countries that have an area of greater than 2,000,000 km^2
import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()
# cur.execute("SELECT country FROM countries WHERE area >= 2000000")
cur.execute("SELECT * FROM countries")
rows = cur.fetchall()
conn.close()
# print(rows)

print("Index --- Country")
for i in rows:
    print( f"{i[0]} --- {i[1]}")
    

