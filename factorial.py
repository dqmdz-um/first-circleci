def factorial(numero: int):
    if numero in (0, 1):
        return 1
    return numero * factorial(numero - 1)
