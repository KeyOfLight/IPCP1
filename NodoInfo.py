class NodoInfo:
    def __init__(self, posNombre, posFilas, posColumas, posLista,PosListaFrecuencia):
        self.nombre = posNombre
        self.filas = posFilas
        self.columnas = posColumas
        self.Lista = posLista
        self.siguiente = None
        self.ListaNoFrecuencia = PosListaFrecuencia