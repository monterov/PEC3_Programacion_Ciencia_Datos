import math
import time

def calcular_factorial(num: int) -> int:
    """
    Computes the factorial of the given integer.

    Args:
        num (int): number to  be calculated.

    Returns: 
        (int): The factorial of nun.
    """
    return math.factorial(num)

# Versión secuencial

def factorial_secuencial(nums: list[int]) -> list[int]:
    """
    Computes the factorial of a list of integers sequentially and measures execution time.

    Args:
        nums (list[int]): list of numbers to be calculated.

    Returns:
        (list[int]): list with the factorial of each number.
    """
    # Marcamos el inicio del contador de tiempo
    
    inicio_tiempo = time.perf_counter()
    resultados = []

    # Bucle para el cálculo secuencial

    for n in nums:
        resultados.append(calcular_factorial(n))

    # Calculamos el tiempo total transcurrido

    tiempo_ejecucion = time.perf_counter() - inicio_tiempo
    print(f"Tiempo secuencial: {tiempo_ejecucion:.6f} segundos")

    return resultados    

# Ejecución función factorial_secuencial

nums = [150000, 200000, 250000, 300000, 350000, 400000]

res_seq = factorial_secuencial(nums)
print("Resultados calculados (secuencial):", len(res_seq))

# Ejecución función factorial_multiproceso

nums = [150000, 200000, 250000, 300000, 350000, 400000]

res_mp = factorial_multiproceso(nums)
print("Resultados calculados (multiproceso):", len(res_mp))


