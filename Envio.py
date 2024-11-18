class Envio:
    def __init__(self, orden, costo):
        self.orden = orden
        self.costo = costo
        
        
class Delivery(Envio):
    def __init__(self, orden, costo, nombre, id, telefono):
        super().__init__(orden, costo)
        self.nombre = nombre
        self.id = id
        self.telefono = telefono