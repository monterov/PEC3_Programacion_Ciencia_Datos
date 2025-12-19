## Ejercicio 3
En este ejercicio detectaréis las ineficiencias y mejoraréis el código. En este caso, vamos a analizar el cálculo de la suma de los factoriales de los primeros n números naturales.

### Ejercicio 3.1 
Utilizando las herramientas de profiling que hemos visto en el Notebook de teoría, analizad el siguiente fragmento de código ineficiente y encontrad cual es el cuello de botella. Explicad las ineficiencias que habéis detectado, relacionándolas con los resultados obtenidos en el profiling.

#### Vamos a usar  las herramientas de análisis de rendimiento: %timeit y %lprun.

**Resultado %timeit**

4.12 s ± 738 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

**Resultado %lprun**
![Resultado_%lprun](pantallazo_10.png)

#### Conclusión

El cuello de botella del código se encuentra en la operación fact *= j. Esta línea concentra la mayor parte del tiempo de ejecución (≈64%), ya que se ejecuta un número muy elevado de veces debido al uso de bucles anidados (como en el caso del algoritmo del ejercicio 1) y a la recomputación completa del factorial para cada valor de i.

En consecuencia, el número de operaciones crece de forma cuadrática con n (complejidad temporal O(n²)), lo que explica el elevado tiempo de ejecución cuando n toma valores relativamente grandes, como en la prueba realizada.

### Ejercicio 3.2 

Mejorad el código con el objetivo de reducir el tiempo de ejecución. Además, comentad la mejora realizada, indicando la complejidad temporal y si ésta ha mejorado respecto a la versión anterior.

![Resultado_%lprun_mejorado](pantallazo_11.png)

