class Venta:
    def __init__(self, cliente, productos, cantidad, metodo_pago, metodo_envio, total):
        self.cliente = cliente
        self.productos = productos
        self.cantidad = cantidad
        self.metodo_pago = metodo_pago
        self.metodo_envio = metodo_envio
        self.total = total
        
