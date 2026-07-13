from matematicas.calculo_areas import *
from matematicas.operaciones import sumar, restar

def main():
    area_circulo = calcular_area_circulo(4)
    area_rectangulo = calcular_area_rectangulo(5, 3)
    print(F"El área del círculo es: {area_circulo}")
    print(F"El área del rectángulo es: {area_rectangulo}")
    sumar(5, 3)
    restar(10, 4)
    
main()