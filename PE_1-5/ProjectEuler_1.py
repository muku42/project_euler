# CS294 Python, University of Hawaii at Hilo, Fall 2015
# David L. Bennett
# Module #11 Hone: Project Euler

# Problem #1 "Multiples of 3 and 5"

def euler1(n):
    total = 0
    for ii in range(1,n):
        if ii % 3 == 0 or ii % 5 == 0:
            total += ii
    print("\nThe answer to Project Euler Problem #1 is", total, "\n")

euler1(1000)
