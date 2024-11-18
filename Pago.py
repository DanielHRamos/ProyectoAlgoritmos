class Pago:
    def __init__(self, cliente, monto, moneda, tipo, fecha):
        self.cliente = cliente
        self.monto = monto
        self.moneda = moneda
        self.tipo = tipo
        self.fecha = fecha