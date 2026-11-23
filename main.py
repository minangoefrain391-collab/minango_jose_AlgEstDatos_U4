# main.py
# Unidad 4 - Laboratorio de eficiencia: mide, compara y explica cuatro algoritmos.
# Autor: José Efraín Minango Morales
#
# python main.py            -> pruebas + tabla de tiempos y razones (R4)
# python main.py --perfil   -> lo mismo, y además el reporte de cProfile (opcional)

import random
import sys
import time

from algoritmos import (
    burbuja, merge_sort, busqueda_lineal, busqueda_binaria, prueba_algoritmos,
)

TAMANOS = [1000, 2000, 4000, 8000]
CANT_BUSQUEDAS = 1000      # cuántas búsquedas seguidas se cronometran (ver README)
REPETICIONES = 3           # cada medición se repite y se guarda la mejor
SEMILLA = 2026             # para que los datos de cada corrida sean los mismos

# Razón que predije en el R1 al duplicar n (analisis_teorico_r1.md)
PREDICCION = {
    "burbuja": "~4",
    "merge sort": "~2,2",
    "búsqueda lineal": "~2",
    "búsqueda binaria": "~1,0-1,1",
}


# Función de medición entregada por el docente en el enunciado (plantilla del R4).
# La dejé tal cual; solo le agregué abajo mejor_tiempo() para repetir la medición.
def medir(funcion, datos):
    """Devuelve el tiempo en segundos que tarda funcion(datos)."""
    copia = list(datos)
    inicio = time.perf_counter()
    funcion(copia)
    return time.perf_counter() - inicio


def mejor_tiempo(funcion, datos):
    """Repite la medición y se queda con el menor tiempo (el menos afectado por el ruido)."""
    return min(medir(funcion, datos) for _ in range(REPETICIONES))


def buscar_varias(busqueda, lista, objetivos):
    """Hace una búsqueda por cada objetivo. Es lo que se cronometra en R3."""
    for objetivo in objetivos:
        busqueda(lista, objetivo)


def generar_datos(n):
    """Lista de n enteros al azar, como en la plantilla del docente."""
    return [random.randint(1, 10**6) for _ in range(n)]


def medir_todo():
    """Devuelve {nombre_algoritmo: [tiempo por cada tamaño]}."""
    random.seed(SEMILLA)
    tiempos = {nombre: [] for nombre in PREDICCION}
    for n in TAMANOS:
        datos = generar_datos(n)
        objetivos = random.choices(datos, k=CANT_BUSQUEDAS)   # valores que sí están
        ordenados = merge_sort(datos)    # la binaria exige lista ordenada; se ordena
                                         # una vez y ese costo NO entra en su tiempo

        tiempos["burbuja"].append(mejor_tiempo(burbuja, datos))
        tiempos["merge sort"].append(mejor_tiempo(merge_sort, datos))
        tiempos["búsqueda lineal"].append(mejor_tiempo(
            lambda lista: buscar_varias(busqueda_lineal, lista, objetivos), datos))
        tiempos["búsqueda binaria"].append(mejor_tiempo(
            lambda lista: buscar_varias(busqueda_binaria, lista, objetivos), ordenados))
    return tiempos


def imprimir_tablas(tiempos):
    """Una tabla por algoritmo, con el mismo formato de la plantilla, y un resumen."""
    for nombre, lista_tiempos in tiempos.items():
        print(f"\n{nombre}")
        print(f"{'n':>6} {'tiempo(s)':>12} {'razon':>8}")
        anterior = None
        for n, t in zip(TAMANOS, lista_tiempos):
            razon = f"{t/anterior:.2f}" if anterior else "-"
            print(f"{n:>6} {t:>12.5f} {razon:>8}")
            anterior = t

    print("\nResumen de razones (cada medición / la anterior) frente a lo predicho en R1")
    encabezado = f"{'algoritmo':<18}"
    for i in range(1, len(TAMANOS)):
        encabezado += f"{TAMANOS[i-1]}->{TAMANOS[i]:<8}".rjust(13)
    print(encabezado + f"{'predicho':>12}")
    for nombre, lista_tiempos in tiempos.items():
        fila = f"{nombre:<18}"
        for i in range(1, len(TAMANOS)):
            fila += f"{lista_tiempos[i]/lista_tiempos[i-1]:.2f}".rjust(13)
        print(fila + f"{PREDICCION[nombre]:>12}")


def correr():
    prueba_algoritmos()
    print(f"\nMedición: {CANT_BUSQUEDAS} búsquedas por tamaño, mejor de {REPETICIONES} repeticiones.")
    print("Tiempos de burbuja, merge sort y las dos búsquedas con listas al azar:")
    imprimir_tablas(medir_todo())


if __name__ == "__main__":
    if "--perfil" in sys.argv:
        import cProfile
        import pstats
        perfil = cProfile.Profile()
        perfil.runcall(correr)
        print("\n=== cProfile: las 8 funciones con más tiempo acumulado ===")
        pstats.Stats(perfil).sort_stats("cumulative").print_stats(8)
    else:
        correr()
