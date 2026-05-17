"""
Utilidades básicas para pruebas
"""

def saludar(nombre):
    """Devuelve un saludo personalizado"""
    return f"¡Hola, {nombre}!"


def sumar(a, b):
    """Suma dos números"""
    return a + b


def restar(a, b):
    """Resta dos números"""
    return a - b


def multiplicar(a, b):
    """Multiplica dos números"""
    return a * b


def dividir(a, b):
    """Divide dos números"""
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b


def es_par(numero):
    """Verifica si un número es par"""
    return numero % 2 == 0


def lista_al_reves(lista):
    """Devuelve una lista invertida"""
    return lista[::-1]


if __name__ == "__main__":
    # Pruebas básicas
    print(saludar("Usuario"))
    print(f"2 + 3 = {sumar(2, 3)}")
    print(f"10 - 4 = {restar(10, 4)}")
    print(f"5 * 6 = {multiplicar(5, 6)}")
    print(f"20 / 4 = {dividir(20, 4)}")
    print(f"¿7 es par? {es_par(7)}")
    print(f"¿8 es par? {es_par(8)}")
    print(f"Inversa de [1,2,3]: {lista_al_reves([1, 2, 3])}")
