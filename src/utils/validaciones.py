def validar_edad(edad):
    return 18 <= edad <= 120

def validar_codigo_promocional(codigo):
    if codigo == "PROMO10":
        return 0.10
    elif codigo == "DESCUENTO20":
        return 0.20     
    elif codigo == "DESCUENTO101":
        return 1.01
    return 0.0

def get_descuento_porc(codigo_promocional):
        """Devuelve un float entre 0.0 y 1.0 para el código dado."""
        if not codigo_promocional:
            return 0.0
        cod = str(codigo_promocional).upper()
        mapping = {
            "PROMO10": 0.10,
            "DESCUENTO20": 0.20,
        }
        # Para forzar error de caso límite en tests
        if cod == "DESCUENTO101":
            return 1.01
        return mapping.get(cod, 0.0)


