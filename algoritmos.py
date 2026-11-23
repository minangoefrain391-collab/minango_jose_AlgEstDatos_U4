# algoritmos.py
# Los cuatro algoritmos de la Unidad 4: dos de ordenamiento (R2) y dos de búsqueda (R3).
# n es la cantidad de elementos de la lista.
#
# Código adaptado de los ejemplos de la Clase 11 (burbuja, merge_sort/fusionar) y de la
# Clase 12 (búsqueda lineal y binaria) de la materia. Lo que cambié de cada uno está
# indicado en el comentario de la función. Base teórica: Cormen et al. (2022).


# ---------------------------------------------------------------
# R2: ordenamiento
# ---------------------------------------------------------------

def burbuja(lista):
    """Ordena la lista en el lugar y la devuelve."""
    # Adaptado de la burbuja de la Clase 11. Le agregué la bandera hubo_cambio y que
    # i llegue hasta n - 2, para cortar si en una pasada no hubo intercambios.
    # burbuja: O(n^2) promedio y peor caso, O(n) mejor caso (por la bandera)
    # espacio: O(1), solo intercambia dentro de la misma lista
    n = len(lista)
    for i in range(n - 1):
        hubo_cambio = False
        for j in range(n - 1 - i):          # lo que ya subió al final no se revisa
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                hubo_cambio = True
        if not hubo_cambio:                 # una pasada sin cambios = ya está ordenada
            break
    return lista


def merge_sort(lista):
    """Devuelve una lista nueva ordenada (no modifica la original)."""
    # Adaptado del merge_sort de la Clase 11. Cambié el caso base para devolver una copia
    # (así la lista original nunca se modifica) y a fusionar() le puse mezclar().
    # merge sort: O(n log n) en los tres casos
    # espacio: O(n) por las listas auxiliares de la mezcla
    if len(lista) <= 1:
        return lista[:]
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    return mezclar(izquierda, derecha)


def mezclar(izquierda, derecha):
    """Junta dos listas ya ordenadas en una sola ordenada."""
    # mezclar: O(n) con n = len(izquierda) + len(derecha)
    resultado = []
    i = 0
    j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:      # <= para que sea estable con repetidos
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])         # lo que sobre de alguna de las dos
    resultado.extend(derecha[j:])
    return resultado


# ---------------------------------------------------------------
# R3: búsqueda
# ---------------------------------------------------------------

def busqueda_lineal(lista, objetivo):
    """Devuelve la posición del objetivo o -1 si no está."""
    # Adaptado de busqueda_lineal de la Clase 12 (ahí usan enumerate; yo recorro por índice).
    # búsqueda lineal: O(n) promedio y peor caso, O(1) mejor caso
    # espacio: O(1)
    for posicion in range(len(lista)):
        if lista[posicion] == objetivo:
            return posicion
    return -1


def busqueda_binaria(lista, objetivo):
    """Devuelve la posición del objetivo o -1 si no está. La lista debe venir ordenada."""
    # Adaptado de busqueda_binaria de la Clase 12 (mismo método; cambié izq/der por bajo/alto).
    # búsqueda binaria: O(log n) promedio y peor caso, O(1) mejor caso
    # espacio: O(1) porque es iterativa (la recursiva gastaría O(log n) en la pila)
    bajo = 0
    alto = len(lista) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio] == objetivo:
            return medio
        if lista[medio] < objetivo:
            bajo = medio + 1                # descarta la mitad de la izquierda
        else:
            alto = medio - 1                # descarta la mitad de la derecha
    return -1


# ---------------------------------------------------------------
# Pruebas
# ---------------------------------------------------------------

def prueba_algoritmos():
    """Casos de prueba con assert, incluyendo casos límite."""

    casos = [
        [],                         # vacía
        [7],                        # un solo elemento
        [1, 2, 3, 4, 5],            # ya ordenada
        [5, 4, 3, 2, 1],            # al revés
        [3, 1, 3, 2, 1, 3],         # valores repetidos
        [2, 2, 2, 2],               # todos iguales
        [9, -4, 0, 15, -4, 8],      # con negativos
    ]
    for caso in casos:
        esperado = sorted(caso)
        assert burbuja(caso[:]) == esperado
        assert merge_sort(caso) == esperado
    original = [4, 2, 9, 1]
    merge_sort(original)
    assert original == [4, 2, 9, 1]        # merge_sort no toca la original

    # búsquedas sobre una lista ordenada con un repetido
    ordenada = [1, 3, 3, 5, 8, 13, 21]
    for valor in ordenada:
        assert busqueda_lineal(ordenada, valor) != -1
        assert ordenada[busqueda_binaria(ordenada, valor)] == valor
    assert busqueda_lineal(ordenada, 3) == 1            # la lineal da la primera
    assert busqueda_lineal(ordenada, 4) == -1           # no está (en el medio)
    assert busqueda_binaria(ordenada, 4) == -1
    assert busqueda_binaria(ordenada, 0) == -1          # menor que todos
    assert busqueda_binaria(ordenada, 99) == -1         # mayor que todos
    assert busqueda_lineal([], 1) == -1                 # lista vacía
    assert busqueda_binaria([], 1) == -1
    assert busqueda_binaria([6], 6) == 0                # un solo elemento
    assert busqueda_binaria([6], 7) == -1

    print("Todas las pruebas pasaron.")


if __name__ == "__main__":
    prueba_algoritmos()
