def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1

    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b

    return fibonacci_sequence

# Change the value of 'n' to generate a different number of terms.
n = 4
fib_sequence = generate_fibonacci(n)
print(f"Fibonacci sequence with {n} terms: {fib_sequence}")
