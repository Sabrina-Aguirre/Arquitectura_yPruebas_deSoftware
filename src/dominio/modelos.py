class Cliente:
    def __init__(self, nombre: str, email: str):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if "@" not in email or "." not in email:
            raise ValueError("Email inválido.")
        self.nombre = nombre
        self.email = email

    def realizar_pedido(self, producto, cantidad: int, codigo_promocional=None):
        """
        Crea y devuelve un Pedido para este cliente.
        """
        from src.dominio.modelos import Pedido  # import local para evitar problemas si se modifica la estructura
        return Pedido(producto, cantidad, codigo_promocional)

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

        subtotal = self.subtotal
        from src.utils.validaciones import get_descuento_porc
        descuento_porc = get_descuento_porc(self.codigo_promocional) if self.codigo_promocional else 0.0
        if descuento_porc > 1.0:
            raise ValueError("El porcentaje de descuento no puede ser mayor que 100%.")
        return subtotal * (1 - descuento_porc)
    