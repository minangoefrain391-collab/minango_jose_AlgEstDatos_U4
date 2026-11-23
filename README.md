# Unidad 4: análisis de algoritmos (ordenamiento y búsqueda)

Tarea de Algoritmos y Estructuras de Datos, Ciencia de Datos, Universidad Politécnica Salesiana.
Autor: José Efraín Minango Morales. Docente: Miguel Ángel Quiroz Martínez.

Comparo cuatro algoritmos: primero predije cómo debían crecer los tiempos (R1) y después los medí
con listas de 1.000, 2.000, 4.000 y 8.000 elementos (R4).

## Cómo ejecutarlo

Solo usa la biblioteca estándar de Python (probado con Python 3.13).

```
python main.py            # pruebas + tablas de tiempos y razones
python main.py --perfil   # lo mismo + reporte de cProfile (opcional)
```

Tarda unos 10 segundos, casi todo es la burbuja con 8.000 elementos.

## Archivos

| Archivo | Qué tiene |
|---|---|
| `analisis_teorico_r1.md` | Análisis teórico previo (R1). Lo escribí antes de medir y no lo modifiqué. |
| `algoritmos.py` | Los cuatro algoritmos, con su complejidad en comentarios, y las pruebas. |
| `main.py` | Medición (R4): función `medir` de la plantilla del docente, tablas y razones. |
| `resultados_corrida.txt` | Salida real de una corrida de `python main.py`. |
| `resultados_cprofile.txt` | Salida real de `python main.py --perfil`. |

## Algoritmos

- **Burbuja** (ordenamiento simple, R2). Con una bandera que corta si una pasada no hizo cambios.
- **Merge Sort** (ordenamiento eficiente, R2). Recursivo, con una función `mezclar`.
- **Búsqueda lineal** (R3).
- **Búsqueda binaria** (R3). Iterativa; recibe la lista ya ordenada con Merge Sort.

El código de burbuja, Merge Sort y las dos búsquedas está adaptado de los ejemplos de las
Clases 11 y 12; en cada función dejé escrito qué cambié.

## Decisiones de la medición

- Uso `time.perf_counter()` y la función `medir(funcion, datos)` de la plantilla, tal cual,
  que trabaja sobre una copia de la lista.
- Cada medición se repite 3 veces y me quedo con la menor, para reducir el ruido de otros
  procesos del computador.
- Los datos son enteros al azar con semilla fija (2026), así que cada corrida parte de las
  mismas listas.
- Una sola búsqueda dura microsegundos y no se distingue del ruido. Por eso cronometro
  **1.000 búsquedas seguidas** de valores que sí están en la lista.
- La búsqueda binaria necesita la lista ordenada. La ordeno una vez con Merge Sort fuera del
  cronómetro; ese costo, O(n log n), no entra en su tiempo.

## R1: análisis teórico previo

| Algoritmo | Tiempo | Espacio | Razón esperada al duplicar n |
|---|---|---|---|
| Burbuja | O(n²); mejor caso O(n) | O(1) | ≈ 4 |
| Merge Sort | O(n log n) | O(n) | ≈ 2,2 (2,17 a 2,20) |
| Búsqueda lineal | O(n); mejor caso O(1) | O(1) | ≈ 2 |
| Búsqueda binaria | O(log n); mejor caso O(1) | O(1) | 1,0 a 1,1 |

El detalle y la justificación están en `analisis_teorico_r1.md`.

## R4: resultados de una corrida

Estos números salen de `resultados_corrida.txt` (Python 3.13 sobre Linux, 2 núcleos). En otro
computador los tiempos serán distintos; lo que debe parecerse son las razones.

| n | Burbuja (s) | Merge Sort (s) | B. lineal (s) | B. binaria (s) |
|---|---|---|---|---|
| 1.000 | 0,03538 | 0,00121 | 0,01482 | 0,00094 |
| 2.000 | 0,14094 (3,98) | 0,00273 (2,26) | 0,02400 (1,62) | 0,00107 (1,13) |
| 4.000 | 0,58735 (4,17) | 0,00597 (2,19) | 0,04949 (2,06) | 0,00117 (1,09) |
| 8.000 | 2,43898 (4,15) | 0,01245 (2,09) | 0,10151 (2,05) | 0,00125 (1,07) |

Entre paréntesis, la razón respecto a la medición anterior.

**¿Se cumplió la predicción?** En general sí: burbuja cerca de 4, Merge Sort y lineal cerca de
2, binaria apenas sobre 1 (Tabla 16 de la Clase 12). Dos diferencias:

- La búsqueda lineal dio 1,62 en el primer paso. Revisé los datos: con la semilla 2026, las
  1.000 búsquedas hacen 1,97 veces más comparaciones al pasar de 1.000 a 2.000, así que el
  trabajo sí se duplica. En tres corridas completas esa razón salió 1,62, 1,59 y 1,96. No
  identifiqué la causa.
- La binaria dio 1,13 en el primer paso, un poco sobre mi límite de 1,1, y Merge Sort dio 2,09
  al final, bajo el rango 2,17 a 2,20 que calculé.

**cProfile.** En `resultados_cprofile.txt` la burbuja ocupa 9,83 s de los 11,21 s de la
corrida: es el cuello de botella. Merge Sort ocupa 0,76 s en total. Con el perfilador activo
todo corre más lento, así que esa corrida sirve para ver dónde se va el tiempo
y no para comparar las razones.

## Referencias

Cormen, T. H., Leiserson, C. E., Rivest, R. L., y Stein, C. (2022). *Introduction to
algorithms* (4.ª ed.). MIT Press.

Skiena, S. S. (2020). *The algorithm design manual* (3.ª ed.). Springer.
