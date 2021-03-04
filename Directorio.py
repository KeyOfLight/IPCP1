from xml.dom import minidom
from ListaCir import ListaC
from MatrizAnalizador import MatrizAnalizador
import xml.etree.cElementTree as ET
from ListaSimple import ListaSimple
from os import remove
class Directorio:
    def __init__(self, rutaDelArchivo):
        self.NombreDelArchivo =  rutaDelArchivo
        self.archivoXml = minidom.parse(rutaDelArchivo)
        self.ListasMatricesReducidas = ListaSimple()
        self.Lista = ListaSimple()

    def ObtenerListas(self):
        return self.Lista

    def VerCaminoNN(self, PathCompleto):
        longitud = len(PathCompleto.split('/'))
        nombre =PathCompleto.split('/')[longitud-1]
        pathSinNobre = PathCompleto.replace(nombre,"")
        return pathSinNobre


    def LeerArchivo(self):
        
        Lista = ListaC()
        for matriz in self.archivoXml.getElementsByTagName("matriz"):
            NombreM=matriz.getAttribute("nombre")
            print("Analizando matriz: " + NombreM)
            tuplas = int(matriz.getAttribute("n"))
            columnas = int(matriz.getAttribute("m"))
            print(" >tuplas=" + str(matriz.getAttribute("n")))
            print(" >columnas=" + str(matriz.getAttribute("m")))
            for Elemento in matriz.getElementsByTagName("dato"):
                Dato = int(Elemento.firstChild.data)
                Fila = int(Elemento.getAttribute("x"))
                columna = int(Elemento.getAttribute("y"))
                Lista.Agregar(Dato, columna, Fila)
            Ana = MatrizAnalizador(Lista,tuplas,columnas)
            Ana.ConvertirABinaria()
            Ana.CompararTuplasDeMatrizBinaria()
            Ana.addTuplaNoSumadas()
            print("*********************************************************************")
            self.Lista.AgregarINFORMACION(NombreM, tuplas, columnas,Lista, None)
            self.ListasMatricesReducidas.AgregarINFORMACION(NombreM, Ana.getTuplaTotales(), columnas, Ana.getMatrizFrecuencia(), Ana.RegistroDeFrecuencias)


    def RETake(self, path):
        Archivo = open( path +"cache.xml", encoding='utf-8')
        ArchivoFrec = open(path+"frecuencias.xml","w",encoding='utf-8')
        linea = Archivo.readline()
        lineaFormateada = linea.replace("</matriz>", "\n</matriz>")
        lineaFormateada = lineaFormateada.replace("<matriz", " \n<matriz")
        lineaFormateada = lineaFormateada.replace("<dato", "\n       <datos")
        lineaFormateada = lineaFormateada.replace("</matrices>", "\n</matrices>")
        lineaFormateada = lineaFormateada.replace("<frecuenci", "\n       <frecuenci")
        for linea2 in lineaFormateada.split("\n"):
            ArchivoFrec.write(linea2 + "\n") 
        ArchivoFrec.close()
        Archivo.close()
        remove(path +"cache.xml")
    
    def EscribirArchivo(self, CaminoNn):
        auxiliar = self.ListasMatricesReducidas.Inicio
        Camino = CaminoNn
        matrices  = ET.Element("matrices")
        while auxiliar != None:
            nombre =  auxiliar.nombre
            filas = auxiliar.filas
            columnas = auxiliar.columnas
            doc = ET.SubElement(matrices, "matriz", m=str(columnas), n=str(filas),  nombre= nombre)
            auxiliarDatos = auxiliar.Lista.ultimo.siguiente
            for fila in range(int(filas)):
                fila = fila+1
                for columa in range(int(columnas)):
                    columa = columa+1
                    ET.SubElement(doc, "dato", y=str(columa), x= str(fila)).text= str(auxiliarDatos.dato)
                    auxiliarDatos = auxiliarDatos.siguiente
            listaDeFrecuencias = auxiliar.ListaNoFrecuencia
            auxListaDeFrecu = listaDeFrecuencias.Inicio
            contadorDeFilas=0
            while auxListaDeFrecu != None:
                ET.SubElement(doc, "frecuencia", g=str(contadorDeFilas+1)).text = str(auxListaDeFrecu.dato)
                auxListaDeFrecu = auxListaDeFrecu.siguiente
                contadorDeFilas=contadorDeFilas+1
            auxiliar = auxiliar.siguiente
        Archivo = ET.ElementTree(matrices)
        Archivo.write(Camino + "cache.xml")
        self.RETake(CaminoNn)
        
        