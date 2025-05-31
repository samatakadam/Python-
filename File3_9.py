import multiprocessing
import math

def compute_factorial(n):
    """Compute the factorial of a number."""
    return math.factorial(n)

if __name__ == "__main__":
    
    numbers = [5, 7, 10, 12, 15]

   
    with multiprocessing.Pool() as pool:
       
        results = pool.map(compute_factorial, numbers)

   
    for num, fact in zip(numbers, results):
        print(f"Factorial of {num} is {fact}")
