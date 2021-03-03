# Interfaz del usuario
from ListaCir import ListaC
from Archivo import Archivo
listaCircular = ListaC()
from Grafico import Grafico
opcion = 0

#comentario
Camino = ""
while opcion!=6:
    print("===============================================")
    print("|                MENU PRINCIPAL               |")
    print("|                                             |")
    print("| 1. CARGAR ARCHIVO                           |")
    print("| 2. PROCESAR ARCHIVO                         |")
    print("| 3. ESCRIBIR ARCHIVO DE SALIDA               |")
    print("| 4. MOSTRAR DATOS DEL ESTUDIANTE             |")
    print("| 5. GENERAR GRAFICA                          |")
    print("| 6. SALIR                                    |")
    print("|                                             |")
    print("===============================================")
    opcion = int(input())

    if opcion == 1:
        print("***********************************************")
        print("| Ingrese la ruta del archivo                 |")
        print("***********************************************")
        path = input("--------->")
        archivo = Archivo(path)
        Camino = archivo.VerCaminoNN(path)
        print("se ha leído el archivo correctamente")

