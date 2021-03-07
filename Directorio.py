from ListaCircular import ListaC
import xml.etree.cElementTree as ET
from ListaSimple import ListaSimple
from ProcesarMatriz import ProcesarMatriz
import os
from os import remove
from xml.dom import minidom
class Directorio:
    def __init__(self, rutaDelArchivo):
        self.NombreDelArchivo =  rutaDelArchivo
        self.archivoXml = minidom.parse(rutaDelArchivo)
        self.ListasMatricesReducidas = ListaSimple()
        self.Lista = ListaSimple()

    def ObtenerListas(self):
        return self.Lista

    def VerCaminoNN(self, CaminoCompleto):
        longitud = len(CaminoCompleto.split('/'))
        nombre =CaminoCompleto.split('/')[longitud-1]
        CaminoN = CaminoCompleto.replace(nombre,"")
        return CaminoN


    def LeerArchivo(self):
        
        Lista = ListaC()
        for matriz in self.archivoXml.getElementsByTagName("matriz"):
            NombreM=matriz.getAttribute("nombre")
            print("Analizando matriz: " + NombreM)
            Filas = int(matriz.getAttribute("n"))
            columnas = int(matriz.getAttribute("m"))
            for Elemento in matriz.getElementsByTagName("dato"):
                Dato = int(Elemento.firstChild.data)
                Fila = int(Elemento.getAttribute("x"))
                columna = int(Elemento.getAttribute("y"))
                Lista.Agregar(Dato, columna, Fila)
            Ana = ProcesarMatriz(Lista,Filas,columnas)
            Ana.ABinaria()
            Ana.CompararTBinarias()
            Ana.addTuplaNoSumadas()
            self.Lista.AgregarINFORMACION(NombreM, Filas, columnas,Lista, None)
            self.ListasMatricesReducidas.AgregarINFORMACION(NombreM, Ana.getTuplaTotales(), columnas, Ana.ObtenerMF(), Ana.FrecuenciasRegistradas)


    def RETake(self, path):
        Archivo = open( path +"cache.xml", encoding='utf-8')
        ArchivoFrec = open(path+"frecuencias.xml","w",encoding='utf-8')
        linea = Archivo.readline()
        Lineacambiada = linea.replace("</matriz>", "\n</matriz>")
        Lineacambiada = Lineacambiada.replace("<matriz", " \n<matriz")
        Lineacambiada = Lineacambiada.replace("<dato", "\n       <datos")
        Lineacambiada = Lineacambiada.replace("</matrices>", "\n</matrices>")
        Lineacambiada = Lineacambiada.replace("<frecuenci", "\n       <frecuenci")
        for linea2 in Lineacambiada.split("\n"):
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
            ListaF = auxiliar.ListaNoFrecuencia
            AuxListaF = ListaF.Inicio
            contadorDeFilas=0
            while AuxListaF != None:
                ET.SubElement(doc, "frecuencia", g=str(contadorDeFilas+1)).text = str(AuxListaF.dato)
                AuxListaF = AuxListaF.siguiente
                contadorDeFilas=contadorDeFilas+1
            auxiliar = auxiliar.siguiente
        Archivo = ET.ElementTree(matrices)
        Archivo.write(Camino + "cache.xml")
        self.RETake(CaminoNn)
        
        