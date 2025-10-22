from src.servicios.servicio_pedidos import ServicioPedidos

def main():
    print("Bienvenido a la Tienda Online")

    nombre = input("Nombre del producto: ")
    precio = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad: "))
    edad = int(input("Edad del comprador: "))
    codigo = input("Código promocional (opcional): ") or None

    servicio = ServicioPedidos()

    try:
        pedido = servicio.procesar_pedido(nombre, precio, cantidad, edad, codigo)
        print("\n Pedido procesado con éxito")
        print(f"Subtotal: ${pedido.subtotal:.2f}")
        print(f"Total con descuento: ${pedido.total:.2f}")
    except ValueError as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    main()
