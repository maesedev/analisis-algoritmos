from time import time
import sys
sys.setrecursionlimit(200000)

##############################################################
########### Aproximacion de complejidad por tiempo ###########
##############################################################

def factorial(n):
    res = 1
    while n> 1:
        res *= n
        n -= 1
    return res


def fact_r (n):
    if n == 1:
        return 1
    return n * fact_r(n-1)


if __name__ == "__main__":
    n = 50000

    start = time()
    factorial(n)
    end = time()

    print(f"time: {end - start}")

    start = time()
    fact_r(n)
    end = time()
    print(f"time: {end - start}")