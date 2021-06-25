import mysql.connector as c 
db=c.connect(host='localhost',database='school',user='root',passwd='12345')
mc=db.cursor()
mc.execute("insert into library values (8,'Informatics practices class 12','Preeti Arora','Computer')")
# same commands as in mysql 
db.commit()


