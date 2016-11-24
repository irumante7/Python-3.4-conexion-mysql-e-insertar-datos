# Inmobiliaria Primera Parte // Ignacio Rumante A.
import conexion

def bienvenidos():
    print("Bienvenido a Gestion Inmobiliaria Rumante Aiep 2016")
    print("Selecciona una opción:")
    print("1 - Añadir una propiedad")
    print("2 - Listar las propiedades")
    print("3 - Buscar por ID")

def escribir():
    print("Has elegido añadir una propiedad")
    nombre =str(input("Introduce el nombre de la propiedad: "))
    descripcion =str(input("Introduce la descripcion: "))

    #Crear un diccionario para transformar las variables y tomar los input.
    diccionario = {'var1':nombre,
                   'var2':descripcion}

    #conexion.conectando() tambien nos sirve ya que estariamos importando def conectando de conexion.
    import mysql.connector
    con = mysql.connector.connect(user="root",password="",host="127.0.0.1",database="guia3taller")
    cursor=con.cursor()
    
    #Se ejecuta la insercion de datos, utilizando como interfaz el diccionario de datos que
    #llama a las variables

    cursor.execute("""INSERT INTO propiedad (nombre,descripcion) VALUES (%(var1)s,%(var2)s)""",diccionario)
    #con la funcion commit, hacemos que inserte los datos.
    con.commit()
    con.close()
    #Luego se cierra la conexion de dichos parametros.

def listar(fin):
    print("Has elegido listar el contenido de propiedades")
    conexion.conectando()
#    cursor.execute("select * from propiedad")
#rows = cursor.fetchall()
#    for row in rows:
#    print(row)
#    cursor.close()
#    con.close()

def mierror():
    print("La opción que has seleccionado no es válida")

def buscador(nombrebuscado):
    print("Aqui buscaré las coincidencias")
    #Aca realizamos los script de busqueda por id con un Where = ' numero '
