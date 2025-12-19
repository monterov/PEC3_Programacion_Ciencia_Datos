#n Algoritmo original del ejercicio

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

# Algoritmo mejorado

def has_duplicates_improved(num_list: list[int]) -> bool:
    """
    Checks whether a list of ints contains duplicate values using a set.

    Args:
        num_list (list[int]): List of integers to analyze.

    Returns:
        bool: True if duplicates are found, False otherwise.
    """
    seen = set()
    for num in num_list:
        if num in seen:
            return True
        seen.add(num)
    return False

# Lista de pruebas

# Listas de prueba

prueba_sin_duplicados = [3, 7, 12, 25, 41]
prueba_con_duplicados = [5, 9, 2, 9, 14]

# Verificamos usando assert

assert has_duplicates(prueba_sin_duplicados) == has_duplicates_improved(prueba_sin_duplicados)
assert has_duplicates(prueba_con_duplicados) == has_duplicates_improved(prueba_con_duplicados)

print("Ambas funciones producen el mismo resultado")

# Comprobación tiempos de ejecución de ambos algoritmos

import time

sizes = [200, 600, 1000, 1400, 1800, 5000]

tiempo_algoritmo_original = []
tiempo_algoritmo_mejorado = []

for n in sizes:
    data = list(range(n))  # Creamos lista de números sin repetir

    # Medimos el tiempo del algoritmo original

    start = time.perf_counter()
    has_duplicates(data)
    end = time.perf_counter()    
    tiempo_algoritmo_original.append(end - start)

    # Medimos el tiempo del algoritmo mejorado

    start = time.perf_counter()
    has_duplicates_improved(data)
    end = time.perf_counter()
    tiempo_algoritmo_mejorado.append(end - start)

print("Tiempos original:", tiempo_algoritmo_original)
print("Tiempos mejorado:", tiempo_algoritmo_mejorado)

# Gráficas


plt.plot(sizes, tiempo_algoritmo_original, marker="o", label="Algoritmo original")
plt.plot(sizes, tiempo_algoritmo_mejorado, marker="o", label="Algoritmo mejorado")
plt.xlabel("Tamaño de la lista")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Comparación de tiempos entre los algoritmos")
plt.legend()
plt.grid(True)
plt.show()
