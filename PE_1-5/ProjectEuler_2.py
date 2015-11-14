# CS294 Python, University of Hawaii at Hilo, Fall 2015
# David L. Bennett
# Module #11 Hone: Project Euler

# Problem #2 "Even Fibonacci Numbers"

def euler2(n):

    fibo_a = 1
    fibo_b = 2
    fibo_c = 0
    fibo_even = 2

    while fibo_c < n:
        fibo_c = fibo_a + fibo_b
        if fibo_c % 2 == 0:
            fibo_even += fibo_c
        fibo_a = fibo_b
        fibo_b = fibo_c

    print("\nThe answer to Project Euler Problem #2 is", fibo_even, "\n")

euler2(4e6)
