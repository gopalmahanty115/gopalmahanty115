import sqlite3

conn = sqlite3.connect('hello.db')
c = conn.cursor()
#c.execute("""CREATE TABLE movies (
 #         name text,
 #          actor text,
   #        actress text,
   #        director text,
   #        YearOfRelease number)""")
#c.execute("INSERT INTO movies VALUES ('Don', 'Sarookh', 'katrina', 'probhudeba', 2013)")
c.execute("INSERT INTO movies VALUES ('Don', 'Sarookh', 'katrina', 'probhudeba', 2010)")

c.execute("INSERT INTO movies VALUES ('Don', 'Sarookh', 'katrina', 'aditya', 2009)")

c.execute("INSERT INTO movies VALUES ('Don1', 'rajesh', 'shila', 'probhudeba', 2008)")
c.execute("INSERT INTO movies VALUES ('hello', 'modi', 'priyanka', 'chitra', 2011)")
c.execute("INSERT INTO movies VALUES ('crazy', 'shilesh', 'tulasi', 'probhudeba', 2017)")
c.execute("INSERT INTO movies VALUES ('Fell in lov', 'deepak', 'minakshee', 'probhudeba', 2016)")
c.execute("INSERT INTO movies VALUES ('fight', 'Umakant', 'nisha', 'probhudeba', 2015)")
c.execute("INSERT INTO movies VALUES ('dream11', 'shivam', 'sujata', 'gopal', 2013)")
c.execute("INSERT INTO movies VALUES ('Secret', 'kanha', 'afrin', 'Aditya', 2009)")
c.execute("INSERT INTO movies VALUES ('helloworld', 'gopal', 'payal', 'chitra', 2007)")
c.execute("INSERT INTO movies VALUES ('Your name', 'ranvir', 'Aisu', 'sekhar', 2008)")
c.execute("INSERT INTO movies VALUES ('jadoo', 'ali', 'liza', 'swapna', 2010)")
c.execute("INSERT INTO movies VALUES ('Ramayan', 'rakesh', 'kalina', 'john', 2009)")c.execute("INSERT INTO movies VALUES ('sports', 'Ram', 'sonali', 'gopal', 2016)")


#c.execute("INSERT INTO movies VALUES ('bangbang', 'salman', 'Alia', 'badshah', 2019)")

#c.execute("SELECT * FROM movies WHERE name='Don'")
#c.execute("UPDATE movies SET name='Shersaha', actor='Vidutjamal',actress='sania' WHERE name='bangbang'")
c.execute("DELETE FROM movies WHERE name='bangbang'")
c.execute("SELECT * FROM movies")
print(c.fetchall())
conn.commit()
conn.close()

          





