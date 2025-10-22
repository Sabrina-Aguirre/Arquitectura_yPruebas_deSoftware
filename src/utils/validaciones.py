def validar_edad(edad):
    return 18 <= edad <= 120

def validar_codigo_promocional(codigo):
    codigos_validos = ["PROMO10", "DESCUENTO20"]
    return codigo in codigos_validos
