# CS294 Python, University of Hawaii at Hilo, Fall 2015
# David L. Bennett
# Module #11 Hone: Project Euler

# Problem #5 "Smallest Multiple"

def smallest_multiple(n):
    multiple = n
    veritas = range(n, 1, -1)
    while True:
        for ii in veritas:
            modulo = multiple % ii
            if modulo != 0:
                break
        else:
            break
        multiple += n
    print("\nThe answer to Project Euler Problem #5 is",
           multiple, "\n")

smallest_multiple(20)
