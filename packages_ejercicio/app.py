from clientes.buscar import buscar_cliente
from clientes.datos import base_datos


def main():
    nombre = input("Ingrese el nombre del cliente: ")
    cliente, datos = buscar_cliente(nombre)
    if cliente:
        print(f"Datos: {datos}")
    else:
        print("Cliente no encontrado")


main()