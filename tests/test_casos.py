import unittest
from src.dominio.modelos import Producto, Pedido
from src.utils.validaciones import validar_edad, validar_codigo_promocional
from src.servicios.servicio_pedidos import ServicioPedidos

class TestCasos(unittest.TestCase):

    # C1: calcular subtotal normal (2 x 50.0 -> 100.0)
    def test_calcular_subtotal_valido(self):
        producto = Producto("Remera", 50.0)
        pedido = Pedido(producto, 2)
        self.assertEqual(pedido.subtotal, 100.0)

    # C2: cantidad 0 o negativa -> ValueError en Pedido.__init__
    def test_calcular_subtotal_cantidad_invalida(self):
        producto = Producto("Pantalon", 50.0)
        with self.assertRaises(ValueError):
            Pedido(producto, 0)
        with self.assertRaises(ValueError):
            Pedido(producto, -1)

    # C3: aplicar descuento 10% (subtotal 100 -> 90.0) usando código PROMO10
    def test_aplicar_descuento_10porc(self):
        producto = Producto("Remera", 100.0)
        pedido = Pedido(producto, 1, "PROMO10")
        self.assertAlmostEqual(pedido.total, 90.0)

    # C4: aplicar descuento 101% -> se espera ValueError (condición extrema)
    def test_aplicar_descuento_excesivo(self):
        producto = Producto("Remera", 100.0)
        with self.assertRaises(ValueError):  # Cambiar de PermissionError a ValueError
            Pedido(producto, 1, "DESCUENTO101")

    # C5 / C6 / C7 / C8: validar edad (18 -> True, 17 -> False, 120 -> True, 121 -> False)
    def test_validar_edad_limites(self):
        self.assertTrue(validar_edad(18))
        self.assertFalse(validar_edad(17))
        self.assertTrue(validar_edad(120))
        self.assertFalse(validar_edad(121))

    # C9 / C10: validar código promocional (PROMO10 -> 0.1, INVALIDO -> 0.0)
    def test_validar_codigo_promocional(self):
        self.assertAlmostEqual(validar_codigo_promocional("PROMO10"), 0.1)  # 0.1 en vez de 10.0
        self.assertAlmostEqual(validar_codigo_promocional("INVALIDO"), 0.0)

    # C11: integración: procesar pedido cliente 25 + "PROMO10" -> total 90.0 (precio 100, qty 1)
    def test_procesar_pedido_integration_exitoso(self):
        servicio = ServicioPedidos()
        pedido = servicio.procesar_pedido("RemeraPrueba", 100.0, 1, 25, "PROMO10")
        self.assertAlmostEqual(pedido.total, 90.0)

    # C12: integración: cliente 17 + "PROMO10" -> falla temprana por edad
    def test_procesar_pedido_integration_edad_invalida(self):
        servicio = ServicioPedidos()
        with self.assertRaises(PermissionError):
            servicio.procesar_pedido("RemeraPrueba", 100.0, 1, 17, "PROMO10")


if __name__ == "__main__":
    unittest.main()

#para ejecutar posicionarse en la carpeta raíz del proyecto y correr:: python -m unittest tests.test_casos -v