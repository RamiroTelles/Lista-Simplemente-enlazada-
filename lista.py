from operator import truediv
from tkinter.messagebox import NO
from Nodo import Nodo

class lista():

    def __init__(self) -> None:
        self.inicio = None
        self.final = None
        self.Cant = 0

    def agregar(self,dato):
        nuevo = Nodo(dato)
       
        if self.Cant == 0:
            self.inicio = nuevo
            self.final = nuevo
            self.Cant +=1
        else:
            aux = None
            aux = self.inicio
            while(aux.siguiente != None):
                aux = aux.siguiente
            aux.asignarSig(nuevo)
            self.Cant +=1
            self.final = aux.siguiente
        


    def imprimir(self):
        if self.Cant!=0:

            aux = self.inicio
            print(aux.dato)
            while(aux.siguiente!= None):
                aux = aux.siguiente
                print(aux.dato)
        else:
            print("No tiene elementos")

    def buscar(self,x):
        aux = self.inicio
        if aux.dato == x:
            return True
        else:
            while(aux.siguiente!= None):
                aux = aux.siguiente
                if aux.dato == x:
                    return True
            return False
    
    def eliminar(self,pos):
        aux= self.inicio
        i=0
        if pos>(self.Cant-1):
            print("posicion no válida")
            return None
        elif (pos==0):
            aux = aux.siguiente
            self.inicio = aux
        else:
            while(i<pos-1):
                aux = aux.siguiente
                i+=1
            
            aux.asignarSig(aux.siguiente.siguiente)

