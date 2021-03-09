from NodoCircular import NodoCircular
class ListaC:

    def __init__(self):
        self.Last = None
    
    def Add(self, dato, X, Y):
        self.nuevo = NodoCircular(dato, X, Y)

        if self.Last != None:
            self.nuevo.siguiente = self.Last.siguiente
            self.Last.siguiente = self.nuevo
            
        self.Last = self.nuevo
        return self

    def GetPos(self, X, Y):
        auxiliar = self.Last.siguiente
        while True:
            
            if auxiliar.X == Y and auxiliar.Y == X:
                
                return auxiliar.dato
            auxiliar = auxiliar.siguiente
            if auxiliar == self.Last.siguiente:
                break
    
    def VerY(self,Y):
        if self.Last != None:
            auxiliar = self.Last.siguiente

            while True:
                if Y==auxiliar.Y:
                    return True
                
                auxiliar = auxiliar.siguiente
                if auxiliar == self.Last.siguiente:
                    break
        return False
    
    def VerX(self,X):
        if self.Last != None:
            auxiliar = self.Last.siguiente
        
            while True:
                if X==auxiliar.X:
                    return True
            
                auxiliar = auxiliar.siguiente
                if auxiliar == self.Last.siguiente:
                    break
        return False
