from Transacciones import Transacciones

class Libro:
    
    """---------------------
    # Metodos
    ------------------------"""

    def __init__ (self, isbn, titulo, imagen, precioCompra, precioVenta, cantidadActual):

        self.__isbn = isbn
        self.__titulo = titulo
        self.__imagen = imagen
        self.__precioCompra = precioCompra
        self.__precioVenta = precioVenta
        self.__cantidadActual = cantidadActual
        self.__transacciones = [] 

    def getIbn(self):
        return self.__isbn
    
    def setIsbn(self, nIsbn):
        self.__isbn = nIsbn

    def getTitulo(self):
        return self.__titulo
    
    def setTitulo(self, nTitulo):
        self.__titulo = nTitulo
    
    def getImagen(self):
        return self.__imagen
    
    def setImagen(self, nImagen):
        self.__imagen = nImagen

    def getPrecioCompra(self):
        return self.__precioCompra
    
    def setPrecioCompra(self, nPrecioCompra):
        self.__precioCompra = nPrecioCompra

    def getPrecioVenta(self):
        return self.__precioVenta
    
    def setPrecioVenta(self, nPrecioVenta):
        self.__precioVenta = nPrecioVenta
    
    def getCantidadActual(self):
        return self.__cantidadActual
    
    def setCantidadActual(self, nCantidadActual):
        self.__cantidadActual = nCantidadActual
    
    def vender(self, cantidad, fecha):

        vendido = False

        if cantidad <= self.getCantidadActual():

            self.setCantidadActual(self.getCantidadActual()-cantidad)
            nueva = Transacciones(1, cantidad, fecha)
            self.__transacciones.append(nueva)
            vendido = True

        return vendido
    
    def abastecer(self, cantidad, fecha):

        self.setCantidadActual(self.getCantidadActual()+cantidad)
        nueva = Transacciones(2, cantidad, fecha)
        self.__transacciones.append(nueva)
