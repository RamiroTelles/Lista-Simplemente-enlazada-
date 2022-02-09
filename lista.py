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
            self.final = aux.siguiente
        
    #def insertar(self,dato,pos):

     #   if pos ==0:
     #       self.agregar(dato)

     #   elif (pos < (self.Cant-1)):
     #       aux = self.inicio
     #       i=0
     #       nuevo = Nodo(dato)
#            while (i<pos):
#                if((i-1)<pos):
#                    aux.asignarSig(nuevo)

    #            aux = aux.siguiente
    #        nuevo.asignarSig(aux)
    #        aux = nuevo
    #   else:
    #        print("Ingrese una posición válida")
    

    def imprimir(self):
        if self.Cant!=0:

            aux = self.inicio
            print(aux.dato)
            while(aux.siguiente!= None):
                aux = aux.siguiente
                print(aux.dato)
        else:
            print("No tiene elementos")
