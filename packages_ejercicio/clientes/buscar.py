def buscar_cliente(nombre):
    from datos import base_datos
    for cliente, datos in base_datos.items():
        if datos["nombre"] == nombre:
            print(f"Cliente encontrado: {cliente}")
            return cliente, datos
    return None, None

buscar_cliente("maria")