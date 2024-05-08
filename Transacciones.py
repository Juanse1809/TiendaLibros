class transaccion:

    """-----------------
    # Atributos
    --------------------"""
    fecha = ""
    tipo = {
        "abas" : "abastecimiento",
        "ven" : "ventas"
    }
    

    """------------------
    # Metodos
    ---------------------"""
    def __init__(self, pFecha, pTIpo):
        self.__fecha = pFecha
        self.__tipo = pTIpo
        
        
    def getFecha(self):
        return self.__fecha
    
    def getTipo(self):
        return self.__tipo
    

    
    