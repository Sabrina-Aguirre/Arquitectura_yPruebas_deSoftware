from src.dominio.modelos import Producto, Pedido
from src.utils.validaciones import validar_edad, validar_codigo_promocional


class ServicioPedidos:
    """Coordina el proceso de compra."""

    def procesar_pedido(self, nombre_producto, precio, cantidad, edad, codigo=None):
        # Validar edad
        if not validar_edad(edad):
            raise PermissionError("El comprador debe tener entre 18 y 120 años.")
    
        # Crear producto y pedido
        producto = Producto(nombre_producto, precio)
        pedido = Pedido(producto, cantidad, codigo)
        return pedido
