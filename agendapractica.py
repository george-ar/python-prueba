#Agenda telefonica
#v0.1 por gac

#importar archivo externo
import modulos

def principal():
    
    #llamar funcion
    modulos.bienvenidos()

    opcion = input("> ")

    print("Has seleccionado la opción",opcion)

    if opcion == "1":
        modulos.escribir()
        principal()
    elif opcion == "2":
        print("Dime cuantos registros quieres ver:")
        registros = input("> ")
        registrosnumero = int(registros)
        modulos.listar((registrosnumero+1))
        principal()
    elif opcion == "3":
        print("Dime el nombre de la persona que estás buscando:")
        nombrebuscado = input("> ")
        modulos.buscador(nombrebuscado)
        principal()
    else:
        modulos.mierror()
        principal()

principal()
