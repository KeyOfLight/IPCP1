from ListaCir import ListaC
from Directorio import Directorio
listaCircular = ListaC()
from Grafico import Grafico
opcion = 0
Camino = ""

while opcion!=6:
    print("***********************************************")
    print("|                MENU PRINCIPAL               |")
    print("|                                             |")
    print("| 1. CARGAR ARCHIVO                           |")
    print("| 2. PROCESAR ARCHIVO                         |")
    print("| 3. ESCRIBIR ARCHIVO DE SALIDA               |")
    print("| 4. MOSTRAR DATOS DEL ESTUDIANTE             |")
    print("| 5. GENERAR GRAFICA                          |")
    print("| 6. SALIR                                    |")
    print("|                                             |")
    print("***********************************************")
    opcion = int(input())
    if opcion == 1:
        print("***********************************************")
        print("| Ingrese la ruta del archivo                 |")
        print("***********************************************")
        Camino = input("--------->")
        archivo = Directorio(Camino)
        Camino = archivo.VerCaminoNN(Camino)
        print("se ha leído el archivo correctamente")


    elif opcion==2:
        print("***********************************************")
        print("| Se esta procesando el archivo                |")
        print("***********************************************")
        print("procesos:")
        archivo.LeerArchivo()
        listas = archivo.ObtenerListas()


    elif opcion==3:
        print("***********************************************")
        


    elif opcion==4:
        print("***********************************************")


    elif opcion==5:
        if listas != None:
            print("***********************************************")
