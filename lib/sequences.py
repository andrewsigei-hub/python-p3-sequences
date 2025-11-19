#!/usr/bin/env python3

# Prints Fibonacci sequence up to the given length
def print_fibonacci(length):
    fib_sequence = []

    if length == 0:
        print(fib_sequence)
    elif length == 1:
        print([0])
    else:
        # Start sequence with first two numbers
        fib_sequence = [0, 1]

        # Build the rest of the sequence
        while len(fib_sequence) < length:
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)
        
        print(fib_sequence)
