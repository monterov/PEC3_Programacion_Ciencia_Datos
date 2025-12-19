def factorial_sum(n: int):
    """Returns the sum of the factorials of the first n natural numbers.

    Args:
        n (int): Positive integer indicating the upper limit of the factorial sum.

    Returns:
        (int): Sum of factorials from 1! to n!.
    """
    total = 0
    for i in range(1, n + 1):
        fact = 1
        for j in range(1, i + 1):
            fact *= j
        total += fact
    return total

# factorial_sum(3500)

%timeit factorial_sum(3500)

%lprun -f factorial_sum factorial_sum(3500)

def factorial_sum_mejorada(n: int) -> int:
    """Returns the sum of the factorials of the first n natural numbers."""
    total = 0
    fact = 1

    for i in range(1, n + 1): # Como ya tenemos aquí el factorial...
        fact *= i #...lo aprovechamos aquí 
        total += fact

    return total


%timeit factorial_sum_mejorada(3500)

%lprun -f factorial_sum_mejorada factorial_sum_mejorada(3500)
