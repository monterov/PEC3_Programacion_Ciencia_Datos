# Ejercicio 1

En esta serie de ejercicios trabajaremos sobre la eficiencia temporal de los algoritmos. Analizaremos, optimizaremos y compararemos diferentes implementaciones de un problema sencillo: detectar si una lista contiene elementos duplicados.

El objetivo es entender cómo la elección de un enfoque u otro en la implementación puede modificar de forma notable el rendimiento de un algoritmo.
Recordad que el rendimiento de un algoritmo no solo depende del tamaño de la entrada, sino también de sus valores específicos.
Por este motivo, al analizar la eficiencia se suele considerar el caso peor, es decir, aquel en el que el algoritmo requiere el mayor número de operaciones para completarse.


## 1.1 

En este ejercicio debéis analizar la complejidad temporal del siguiente código y expresar su orden de complejidad.
A partir del siguiente algoritmo, determinad su complejidad en notación O, justificando brevemente vuestra respuesta..

def has_duplicates(num_list: list[int]) -> bool:
    """
    Checks whether a list of ints contains duplicate values.

    Args:
        num_list (list[int]): List of integers to analyze.

    Returns:
        bool: True if duplicates are found, False otherwise.
    """
    for k in range(len(num_list)):
        for v in range(k + 1, len(num_list)):
            if num_list[k] == num_list[v]:
                return True
    return False

### Ejercicio 1.1 – Análisis de complejidad temporal

El algoritmo de esta función compara cada elemento de la lista con los siguientes elementos para comprobar si existen valores duplicados. Primero, se selecciona un elemento de la lista y, a continuación, se compara con el resto de los elementos que aparecen después. 
El problema es que el algoritmo va a realizar comparaciones entre todos los pares posibles de elementos cuando no haya valores duplicados. Esto va a hacer que el número de operaciones aumente de forma cuadrática.Si la lista de números es pequeña, no supondrá un problema, pero como la lista sea muy grande, el tiempo de ejecución puede llegar a ser demasiado lento.

#### Referencias

Para resolver este ejercicio he revisado ejemplos de recorridos de listas en los apuntes de la Unidad 4: Optimización de código: complejidad algorítmica y profiling.

Para entender mejor por qué los bucles anidados hacen crecer el número de comparaciones de forma cuadrática, revisé una explicación con un ejemplo de doble bucle en Stack Overflow.

https://stackoverflow.com/questions/64132613/python-complexity-of-on2-number-of-jumps-in-list
