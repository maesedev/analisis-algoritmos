import random
def busqueda_lineal(lista, objetivo):
    match  = False

    for elemento in lista: # O(n)
        if elemento == objetivo:
            match = True
            break
    return match


if __name__ == "__main__":
    tamaño_lista = int(input("De que tamaño la quieres?: "))
    objetivo = int(input("cual es tu objetivo: "))

    lista = [random.randint(0,100) for _ in range (tamaño_lista)]

    print(lista)
    encontrado = busqueda_lineal(lista,objetivo)
    print(f"El elemento {objetivo} {' esta ' if encontrado else ' no esta '}  en la lista")