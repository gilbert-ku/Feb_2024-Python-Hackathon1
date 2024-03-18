def fibonacci(n):
    """
    This function generates the Fibonacci sequence up to a specified term n using iteration.

    Args:
        n: The number of terms in the Fibonacci sequence.

    Returns:
        A list containing the Fibonacci sequence up to n terms.
    """
    if n <= 1:
        # If n is 0 or 1, return [0] or [0, 1] respectively
        fib_sequence = [0, 1][:n+1]  
    else:
        a, b = 0, 1

         # Initialize the sequence with first two terms
        fib_sequence = [0, 1] 
        for _ in range(2, n + 1):
            c = a + b
            a, b = b, c
            fib_sequence.append(c)
    return fib_sequence

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

fibonacci_sequence = fibonacci(num_terms)

print(fibonacci_sequence)
