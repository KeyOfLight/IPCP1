from NodoSimple import NodoSimple
from NodoInfo import NodoInfo
class ListaSimple:
    def __init__(self):
        self.Ultimo = None
        self.Inicio = None
    
    def Agregar(self, Pdato):
        if self.Vacia() == False:
            self.Ultimo.siguiente = NodoSimple(Pdato)
            self.Ultimo = self.Ultimo.siguiente
        else:
            self.Inicio =  self.Ultimo = NodoSimple(Pdato)

    def Vacia(self):
        return self.Inicio == None

    def Mostrar(self):
        auxiliar = self.Inicio
        while auxiliar != None:
            print(str(auxiliar.dato)+ " ", end="")
            auxiliar =  auxiliar.siguiente
        print()
    
    def ExisteEnLista(self, dato):
        if self.Vacia() == False:
            auxiliar = self.Inicio
            while auxiliar != None:
                if auxiliar.dato == dato:
                    return True
                auxiliar =  auxiliar.siguiente
        return False

    def length(self):
        conta = 0
        if self.Vacia() == False:
            auxiliar = self.Inicio
            while auxiliar != None:
                conta = conta + 1
                auxiliar =  auxiliar.siguiente
        return conta

    def AddInfo(self, pNombre, pfilas,pColumas, pLista, PListaFrecuencia):
        if self.Vacia() == False:
            self.Ultimo.siguiente = NodoInfo(pNombre,pfilas,pColumas,pLista,PListaFrecuencia)
            self.Ultimo = self.Ultimo.siguiente
        else:
            self.Inicio =  self.Ultimo = NodoInfo(pNombre,pfilas,pColumas,pLista,PListaFrecuencia)
