class NodoInfo:
    def __init__(self, pNombre, pFilas, pColumas, pLista,PListaFrecuencia):
        self.nombre = pNombre
        self.filas = pFilas
        self.columnas = pColumas
        self.Lista = pLista
        self.siguiente = None
        self.ListaNoFrecuencia = PListaFrecuencia