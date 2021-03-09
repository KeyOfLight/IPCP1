from ListaCircular import ListaC
from Directorio import Directorio
listaCircular = ListaC()
from CreacionGraph import CreacionGraph
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
        archivo.ProcesarArchivo()
        listas = archivo.ObtenerListas()


    elif opcion==3:
        print("||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("|°       Escribiendo archivos de salida         °|")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||")
        archivo.EscribirArchivo(Camino)


    elif opcion==4:
        print("|||||||||||||||||||||||||||||||||||||||||||||||||")
        print("|°                  DATOS                      °|")
        print("|°                DIEGO ANDRÉ GÓMEZ            °|")
        print("|°                  201908327                  °|")
        print("|°INTRODUCCION A LA PROGRAMACION Y COMPUTACION 2 SECCION A°|")
        print("|°       INGENIERIA EN CIENCIAS SISTEMAS       °|")
        print("|°                4to SEMESTRE                 °|")
        print("|||||||||||||||||||||||||||||||||||||||||||||||||")


    elif opcion==5:
        print("||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("|°             CREANDO GRAFICA                  °|")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||")
        x = CreacionGraph(listas,Camino)
        x.CrearGrafico()

    elif opcion ==6:
        break
