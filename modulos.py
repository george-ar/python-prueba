#defenir funcion
def bienvenidos():
    print("Bienvenido a Agenda telefónica")
    print("Selecciona una opción:")
    print("1 - Añadir un registro a la agenda")
    print("2 - Listar el contenido de la agenda")
    print("3 - Buscar por nombre")

def escribir():
    print("Has elegido añadir un registro a la agenda")
    nombre = input("Introduce el nombre de contacto: ")
    telefono = input("Introduce su telefono: ")

    #agenda = open("agendatelefonica.csv",'a')
    agenda = open("agendatelefonica.csv")
    for n in range(1,40):
        linea = agenda.readline()
        lineapartida = linea.split(",")
##        print(lineapartida[0])
        if lineapartida[0] != "":
            memoria = lineapartida[0]
##    print("El numero maximo es",memoria)    
    agenda.close()
    memonum = int(memoria)
    posicion = 0
    posicion = memonum + 1
    postr = str(posicion)
    print("Se ha guardado en la agenda el contacto: s",nombre,"con el numero de telefono",telefono)
    agenda = open("agendatelefonica.csv",'a')
    agenda.write(postr)
    agenda.write(",")
    agenda.write(nombre)
    agenda.write(",")
    agenda.write(telefono)
    agenda.write(",")
    agenda.write("\n")
    agenda.close()

def listar(fin):
    print("Has elegido listar el contenido de la agenda")
    agenda = open("agendatelefonica.csv")
    #for i in range(1,30):
    for i in range(1,fin):
        #print(agenda.readline())
        lectura = agenda.readline()
        print(lectura.replace(",","\t\t"))
    print("ya termine de leer")
    agenda.close()

def mierror():
    print("La opción que has seleccionado no es valida")

def buscador(nombrebuscado):
    print("Aqui buscare las coincidencias")
    agenda = open("agendatelefonica.csv")
    for i in range(1,30):
        lectura = agenda.readline()
        partido = lectura.split(',')
        if nombrebuscado == partido[1]:
            print(partido[2])
    agenda.close()    

