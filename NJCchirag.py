import sqlite3
connection=sqlite3.connect('Movies.db')
cursor=connection.cursor()


command1=""" CREATE TABLE IF NOT EXISTS Movies(name TEXT PRIMARY KEY,actor TEXT,actress TEXT, director TEXT,year INTEGER) """

cursor.execute(command1)


cursor.execute(" INSERT INTO Movies VALUES ('gajini','Aamir khan','Asin','A.R.Murugadoss',2008)")
cursor.execute(" INSERT INTO Movies VALUES ('Don','Amitabh Bachchan','Zeenat Aman','Chandra Barot',1978)")
cursor.execute(" INSERT INTO Movies VALUES ('Dilwale','Sharukh Khan','Kajol','Rohit shetty',2015)")
cursor.execute(" INSERT INTO Movies VALUES ('Main Hoon Na','Sharukh Khan','Sushmita Sen','Farah Khan',2004)")



cursor.execute("SELECT * FROM Movies")
results=cursor.fetchall()


cursor.execute("SELECT * FROM Movies WHERE actor='Amitabh Bachchan' ")
results2=cursor.fetchall()

#print the results
print(results)

print(results2)