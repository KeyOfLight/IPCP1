from ListaCircular import ListaC
from ListaSimple import ListaSimple
import os
class ProcesarMatriz:
    def __init__(self, pListaCiruclar, pfilas, pColumas):
        self.matriz = pListaCiruclar
        self.matrizReducida = ListaC()
        self.matrizBinaria = ListaC()
        self.TuplasRegistradas = ListaSimple()
        self.FrecuenciasRegistradas = ListaSimple()
        self.tuplas = pfilas
        self.columnas = pColumas
        self.frecuencia=0
        self.TuplaConFrecuencia=0
    
    def ABinaria(self):
        print(" > Calculando la matriz binaria")
        Secundaria = self.matriz.Last.siguiente
        while True:
            if Secundaria.dato != 0:
                self.matrizBinaria.Add(1,Secundaria.X, Secundaria.Y)
            else:
                self.matrizBinaria.Add(0,Secundaria.X, Secundaria.Y)
            Secundaria = Secundaria.siguiente
            if Secundaria == self.matriz.Last.siguiente:
                break

    def ObtenerMF(self):
        return self.matrizReducida
    
    def CompararTBinarias(self):
        TuplasIguales = ListaSimple()
        print(" >Realizando suma de tuplas")
        contaFrecuenciaFilas=0
        for noTupla in range(self.tuplas):
            siEncontroTupla = False
            noTupla = noTupla +1
            for tupla2 in range(self.tuplas):
                tupla2 = tupla2 +1
                if noTupla!=tupla2 and self.TuplasRegistradas.ExisteEnLista(tupla2) == False and self.TuplasRegistradas.ExisteEnLista(noTupla)==False:
                    iguales = True
                    for columna in range(self.columnas):
                        columna = columna+1
                        if self.matrizBinaria.GetPos(noTupla,columna) != self.matrizBinaria.GetPos(tupla2,columna,):
                            iguales = False
                            break
                    if iguales:
                        self.TuplasRegistradas.Agregar(tupla2)
                        siEncontroTupla = True
                        TuplasIguales.Agregar(tupla2)
                        contaFrecuenciaFilas=contaFrecuenciaFilas+1
            if siEncontroTupla:
                self.TuplasRegistradas.Agregar(noTupla)
                TuplasIguales.Agregar(noTupla)
                self.SumarTuplas(TuplasIguales)
                TuplasIguales.Inicio = None
                self.FrecuenciasRegistradas.Agregar(contaFrecuenciaFilas+1)
                contaFrecuenciaFilas=0

    def SumarTuplas(self, listaDeTuplasASumar):
        self.frecuencia = self.frecuencia +1
        numero1 = 0
        print("  >sumando tuplas ", end="")
        listaDeTuplasASumar.Mostrar()
        for columna in range(self.columnas):
            columna = columna+1
            for fila in range(self.columnas):
                fila = fila +1
                if listaDeTuplasASumar.ExisteEnLista(fila):
                    numero1=self.matriz.GetPos(fila,columna) + numero1
            self.matrizReducida.Add(numero1,columna, self.frecuencia)
            numero1 = 0

    def NoSumadas(self):
        print(" >Agregando tuplas")
        self.TuplaConFrecuencia = self.frecuencia
        for noTupla in range(self.columnas):
            noTupla=noTupla+1
            if self.TuplasRegistradas.ExisteEnLista(noTupla)==False:
                print(" >agregando tupla " + str(noTupla))
                self.TuplaConFrecuencia=self.TuplaConFrecuencia +1
                self.FrecuenciasRegistradas.Agregar(1)
                for columna in range(self.tuplas):
                    columna=columna+1
                    dato = self.matriz.GetPos(noTupla,columna)
                    self.matrizReducida.Add(dato,columna, self.TuplaConFrecuencia)
        paso = input()
        os.system("cls")


    def getFrecuencia(self):
        return self.frecuencia

    def getTuplaTotales(self):
        return self.TuplaConFrecuencia

    def ListaDeRegistroDeFrecuencias(self):
        return self.FrecuenciasRegistradas
