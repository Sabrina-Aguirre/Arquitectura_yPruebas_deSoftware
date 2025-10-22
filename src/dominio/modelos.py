class Producto:
    def __init__(self, nombre: str, precio_unitario: float):
        if precio_unitario < 0:
            raise ValueError("El precio unitario no puede ser negativo.")
        self.nombre = nombre
        self.precio_unitario = precio_unitario

class Pedido:
    def __init__(self, producto, cantidad, codigo_promocional=None):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        self.producto = producto
        self.cantidad = cantidad
        self.codigo_promocional = codigo_promocional
        self.subtotal = self.calcular_subtotal()
        self.total = self.aplicar_descuento()
    
    def calcular_subtotal(self):
        return self.producto.precio_unitario * self.cantidad
    
    def aplicar_descuento(self):
        if self.codigo_promocional == "PROMO10":
            return self.subtotal * 0.9
        elif self.codigo_promocional == "DESCUENTO20":
            return self.subtotal * 0.8
        return self.subtotal