from Libro import Libro

class tiendaLibros:

    def __init__ (self):
        self.__caja = 1000000
        self.__catalogo = []

    def getCatalogo(self):
        return self.__catalogo
    
    def getCaja(self):
        return self.__caja
    
    def setCaja(self, caja):
        self.__caja = caja

    def buscarLibroPorTitulo(self, titulo):
        LibroBuscado = None

        for Libro in self.__catalogo:
            if Libro.getTitulo() == titulo:
                LibroBuscado = Libro
                break
        
        return LibroBuscado

    def buscarLibroPorIsbn(self, isbn):
        LibroBuscado = None

        for Libro in self.__catalogo:
            if Libro.getIsbn() == isbn:
                LibroBuscado = Libro
                break

        return LibroBuscado

    def registrarLibro(self, isbn, titulo, imagen, precioCompra, precioVenta, cantidadActual):
        
        buscar = self.buscarLibroPorIsbn(isbn)
        nuevo = None

        if buscar == None:
            nuevo = Libro(isbn, titulo, imagen, precioCompra, precioVenta, cantidadActual)
            self.__catalogo.append(nuevo) 

        return nuevo
    

    def EliminarLibro(self, isbn):
        buscar = self.buscarLibroPorIsbn(isbn)
        eliminado = False
        if buscar:
            if buscar.getCantidadActual == 0:
                self.__catalogo.remove(buscar)
                eliminado = True

        return eliminado
    
    def DarLibroMasEconomico(self):
        LibroMasEconomico = None
        if (len(self.__catalogo)>0):

            LibroMasEconomico = self.__catalogo[0]
            for Libro in self.__catalogo:
                if Libro.getPrecioVenta() < LibroMasEconomico.getPrecioVenta():
                    LibroMasEconomico = Libro

        return LibroMasEconomico

    def DarLibroMasCostoso(self):
        LibroMasCostoso = None
        if (len(self.__catalogo)>0):

            LibroMasCostoso = self.__catalogo[0]
            for Libro in self.__catalogo:
                if Libro.getPrecioVenta() > LibroMasCostoso.getPrecioVenta():
                    LibroMasCostoso = Libro

        return LibroMasCostoso
        
    def Vender(self, cantidad, fecha, isbn, titulo=None):
        
        vendido = False
        buscado = self.buscarLibroPorIsbn(isbn)
        
        if titulo is not None and buscado is None:
            buscado = self.buscarLibroPorTitulo(titulo)

        if buscado:
            vendido = buscado.vender(cantidad, fecha)
            self.setCaja(self.getCaja()+(cantidad*buscado.getPrecioVenta()))

        return vendido
    
    def abastecer (self, isbn, cantidad, fecha):
        