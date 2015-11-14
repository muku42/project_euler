# CS294 Python, University of Hawaii at Hilo, Fall 2015
# David L. Bennett
# Module #11 Hone: Project Euler

# Problem #3 "Largest Prime Factor"

def prime_factors(n):
    # Returns all the prime factors of a positive integer
    factors = []
    veritas = 2
    while n > 1:
        while n % veritas == 0:
            factors.append(veritas)
            n /= veritas
        veritas += 1

    print("\nThe answer to Project Euler Problem #3 is", max(factors), "\n")

prime_factors(600851475143)

