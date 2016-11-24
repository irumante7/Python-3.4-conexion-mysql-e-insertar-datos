import mysql.connector

con = mysql.connector.connect(user="root",password="",host="127.0.0.1",database="guia3taller")

cursor=con.cursor()
cursor.execute("INSERT INTO propiedad (id,nombre,descripcion) VALUES ('','Dpto 401','3 dormitorios y dos baños, incluye terraza')")

con.commit()
con.close()
