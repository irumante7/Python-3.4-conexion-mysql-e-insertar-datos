# Gestion Inmobiliaria
# Ignacio Rumante A. - Francisco Moreno
import modulos

def principal():
    modulos.bienvenidos()

    opcion = input("> ")

    print("Has seleccionado la opción",opcion)

    if opcion == "1":
        modulos.escribir()
        principal()
    elif opcion == "2":
        modulos.listar()
        principal()
    elif opcion == "3":
        print("Dime el id que andas buscando:")
        idbuscar = input("> ")
        modulos.buscador(idbuscar)
        principal()
    else:
        modulos.mierror()
        principal()

principal()
