def buscar_cliente(nombre):
    from clientes.datos import base_datos
    for cliente, datos in base_datos.items():
        if datos["nombre"].lower() == nombre.lower():
            return cliente, datos
    return None