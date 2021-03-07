from NodoCircular import NodoCircular
class ListaC:

    def __init__(self):
        self.ultimo = None
    
    def Agregar(self, dato, X, Y):
        self.nuevo = NodoCircular(dato, X, Y)

        if self.ultimo != None:
            self.nuevo.siguiente = self.ultimo.siguiente
            self.ultimo.siguiente = self.nuevo
            
        self.ultimo = self.nuevo
        return self

    def GetPos(self, X, Y):
        auxiliar = self.ultimo.siguiente
        while True:
            
            if auxiliar.X == Y and auxiliar.Y == X:
                
                return auxiliar.dato
            auxiliar = auxiliar.siguiente
            if auxiliar == self.ultimo.siguiente:
                break
    
    def CompararY(self,Y):
        if self.ultimo != None:
            auxiliar = self.ultimo.siguiente

            while True:
                if Y==auxiliar.Y:
                    return True
                
                auxiliar = auxiliar.siguiente
                if auxiliar == self.ultimo.siguiente:
                    break
        return False
    
    def CompararX(self,X):
        if self.ultimo != None:
            auxiliar = self.ultimo.siguiente
        
            while True:
                if X==auxiliar.X:
                    return True
            
                auxiliar = auxiliar.siguiente
                if auxiliar == self.ultimo.siguiente:
                    break
        return False
