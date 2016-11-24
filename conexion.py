def conectando():
    import mysql.connector
    con = mysql.connector.connect(user="root",password="",host="127.0.0.1",database="guia3taller")
    cursor=con.cursor()
