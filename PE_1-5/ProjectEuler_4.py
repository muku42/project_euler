# CS294 Python, University of Hawaii at Hilo, Fall 2015
# David L. Bennett
# Module #11 Hone: Project Euler

# Problem #4 "Largest Palindrome Product"

def euler4(n):
    palindromes = []
    for ii in range(1,n):
        for jj in range(1,n):
            if str(ii*jj) == str(ii*jj)[::-1]:
                palindromes.append(ii*jj)
    print("\nThe answer to Project Euler Problem #4 is",
           max(palindromes), "\n")

euler4(1000)
