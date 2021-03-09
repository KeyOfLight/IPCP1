import os
from os import remove
class CreacionGraph:
    def __init__(self, MatrizFrec, Camino):
        self.MatricesGraph = MatrizFrec
        self.Camino = Camino

    def CrearGrafico(self):
        temporal = self.MatricesGraph.Inicio
        while temporal!= None:
            filas = temporal.filas
            columnas = temporal.columnas
            Archivo = open(self.Camino+temporal.nombre + ".dot", "w", encoding='utf-8')
            Archivo.write("digraph Gramatica{\n")
            Archivo.write("edge[shape=plaintext];\n")
            Archivo.write("Matrices[label = \"Matrices\"]\n")
            Archivo.write("ranksep = 0.1\n")
            Archivo.write("nombre[label = \""+temporal.nombre+"\"]\n")
            Archivo.write("columnas[label = \"m="+str(columnas)+"\", shape=doublecircle,color=blue]\n")
            Archivo.write("filas[label = \"n="+str(filas)+"\",shape=doublecircle,color=blue]\n")
            Archivo.write("Matrices->nombre\n")
            Archivo.write("nombre->filas\n")
            Archivo.write("nombre->columnas\n")
            Contador = 0
            columna = 1
            for fila in range(columnas):
                fila = 1 + fila
                Prev = "nombre"
                for columna in range(filas):
                    columna = columna+1
                    dato = temporal.Lista.GetPos(columna, fila)
                    label = str(dato)
                    Nuevo = str(dato)+str(fila)+str(columna)+str(Contador)
                    Archivo.write(Nuevo+"[label = \""+label+"\"]\n")
                    Archivo.write("ranksep = 0.1\n")
                    Archivo.write(Prev+"->"+Nuevo+"\n")
                    Prev = Nuevo
                Contador=Contador+1
                Prev = None

            Archivo.write("}")
            Archivo.close()
            NombreAr = self.Camino +temporal.nombre
            os.system("dot -Tpdf "+NombreAr+".dot -o "+NombreAr+".pdf")
            remove(NombreAr+".dot")
            temporal = temporal.siguiente

        os.system(NombreAr+".pdf")

