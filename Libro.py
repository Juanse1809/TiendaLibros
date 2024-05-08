class Libro:
    
    """---------------------
    # Metodos
    ------------------------"""

    def __init__ (self, pIsbn, pTitulo, pImagen, pPrecioCompra, pPrecioVenta, pCantidadActual):

        self.__isbn = pIsbn
        self.__titulo = pTitulo
        self.__imagen = pImagen
        self.__precioCompra = pPrecioCompra
        self.__precioVenta = pPrecioVenta
        self.__cantidadActual = pCantidadActual

    def getISBN(self):
        return self.__isbn
    
    def getTitulo(self):
        return self.__titulo
    
    def getImagen(self):
        return self.__imagen
    
    def getPrecioCompra(self):
        return self.__precioCompra
    
    def getPrecioVenta(self):
        return self.__precioVenta
    
    def getCantidadActual(self):
        return self.__cantidadActual
    
