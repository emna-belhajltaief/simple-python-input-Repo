def add(a, b):
    """Retourne la somme de deux nombres"""
    return a + b


def subtract(a, b):
    """Retourne la différence entre deux nombres"""
    return a - b


def multiply(a, b):
    """Retourne le produit de deux nombres"""
    return a * b


def divide(a, b):
    """Retourne la division de a par b"""
    if b == 0:
        raise ValueError("Division par zéro")
    return a / b
