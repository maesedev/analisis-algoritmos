from merge_sort import merge_sort 
from timeit import timeit
import numpy as np

import pyperclip

n = [1000,10000,100000,1000000,10000000]
k = 50
def gen_arr(n):
    return [ np.random.random(10000000) for _ in range(n) ]


def main ():
    times = []
    for i in range(k):
        print(f"\nIteracion {i}")
        arr = gen_arr(n [1] )

        # print("Array original:", arr)

        time = timeit(lambda : merge_sort(arr), number = 300)

        # print("Array ordenado:", arr)
        times.append(time)
        print(time,"sec")
    
    mean_time = sum(times) / len(times)
    print("mean Time: ", str(mean_time).replace(".",","))




if __name__ == "__main__":
    main()

