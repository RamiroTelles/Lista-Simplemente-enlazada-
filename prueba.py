from lista import lista

prueba = lista()

prueba.agregar(1)

prueba.imprimir()
prueba.agregar(2)

prueba.imprimir()

prueba.agregar("Texto")
prueba.agregar("lista en python")

prueba.imprimir()
print("-------------------------------------------------------------")
print(prueba.buscar("Texto"))
print("-----------------------------------------------------------")
prueba.eliminar(3)
prueba.imprimir()