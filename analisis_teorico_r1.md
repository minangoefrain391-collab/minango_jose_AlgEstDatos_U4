## R1: análisis teórico previo

Este apartado lo escribí antes de medir nada y no lo modifico después. n es el tamaño de la lista.

| Algoritmo | Tiempo esperado | Espacio | Justificación |
|---|---|---|---|
| Burbuja | O(n²) en promedio y peor caso; O(n) en el mejor (lista ya ordenada) | O(1) | Dos ciclos anidados comparan pares vecinos: unas n²/2 comparaciones. Con una bandera que corta si una pasada no hizo cambios, la lista ordenada se resuelve en una sola pasada. Ordena en el lugar. |
| Merge Sort | O(n log n) en los tres casos | O(n) | La lista se divide a la mitad log n veces y en cada nivel se mezclan n elementos. La mezcla necesita listas auxiliares. |
| Búsqueda lineal | O(n) en promedio y peor caso; O(1) en el mejor | O(1) | Revisa elemento por elemento hasta encontrar el valor. Si está en una posición al azar, mira en promedio n/2. |
| Búsqueda binaria | O(log n) en promedio y peor caso; O(1) en el mejor | O(1) (versión iterativa) | Descarta la mitad de la lista en cada paso. Exige lista ordenada, y ordenarla antes cuesta O(n log n) una sola vez. |

**Razón esperada al duplicar n** (1.000 → 2.000 → 4.000 → 8.000):

- Burbuja: cerca de 4, porque (2n)² / n² = 4.
- Merge Sort: un poco más de 2, unos 2,2, porque 2n·log(2n) / (n·log n) = 2·(1 + 1/log₂ n) y con n entre 1.000 y 4.000 eso da entre 2,17 y 2,20.
- Búsqueda lineal: cerca de 2.
- Búsqueda binaria: cerca de 1, entre 1,0 y 1,1, porque log(2n)/log(n) es apenas mayor que 1.

Para las dos búsquedas voy a medir 1.000 búsquedas seguidas de valores que sí están en la lista, no una sola, porque una búsqueda aislada dura microsegundos y el reloj no la distingue del ruido. Con una cantidad fija de búsquedas, la razón sigue reflejando el costo de cada una.
