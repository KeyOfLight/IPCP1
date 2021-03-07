from ListaCircular import ListaC
from Directorio import Directorio
listaCircular = ListaC()
from Grafico import Grafico
import os
opcion = 0
Camino = ""

while True:
    print("|||||||||||||||||||||||||||||||||||||||||||||||||")
    print("|°               MENU PRINCIPAL                °|")
    print("|°                                             °|")
    print("|° 1. CARGAR ARCHIVO                           °|")
    print("|° 2. PROCESAR ARCHIVO                         °|")
    print("|° 3. ESCRIBIR ARCHIVO DE SALIDA               °|")
    print("|° 4. MOSTRAR DATOS DEL ESTUDIANTE             °|")
    print("|° 5. GENERAR GRAFICA                          °|")
    print("|° 6. SALIR                                    °|")
    print("|°                                             °|")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||")
    opcion = int(input())
    
    if opcion == 1:
        print("|||||||||||||||||||||||||||||||||||||||||||||||||")
        print("°|          Ingrese la ruta del archivo        °|")
        print("|||||||||||||||||||||||||||||||||||||||||||||||||")
        Camino = input("--------->")
        archivo = Directorio(Camino)
        Camino = archivo.VerCaminoNN(Camino)
        print("Lectura completada")
        paso = input()
        os.system("cls")


    elif opcion==2:
        os.system("cls")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("|°          Procesando el archivo               °|")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("Procesando ")
        archivo.LeerArchivo()
        listas = archivo.ObtenerListas()


    elif opcion==3:
        print("||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("|°       Escribiendo archivos de salida         °|")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||")
        archivo.EscribirArchivo(Camino)


    elif opcion==4:
        print("|||||||||||||||||||||||||||||||||||||||||||||||||")
        print("|°                  DATOS                      °|")
        print("|||||||||||||||||||||||||||||||||||||||||||||||||")


    elif opcion==5:
        print("||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("|°    GENERANDO GRAFICO EN RUTA DEL ARCHIVO     °|")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||")
        x = Grafico(listas,Camino)
        x.CrearGrafico()

    elif opcion ==6:
        break
