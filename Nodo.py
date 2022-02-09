class Nodo():
    
    def __init__(self,dato) -> None:
        self.dato = dato
        self.siguiente = None

    def devolverSig(self):
        return self.siguiente
    
    def asignarSig(self,puntero):
        self.siguiente = puntero
