from merge_sort import merge_sort 
from insertion_sort import insertion_sort
from timeit import timeit
import numpy as np
from datetime import datetime

n = [1000,10000,100000,1000000,10000000]


def gen_arr(n):
    return [ np.random.random() for _ in range(n) ]

def format(float):
    return str(float).replace(".",",")

def main ():
    file_name = f"./sets/set_{datetime.now().timestamp()}.txt"  

    for cant_datos in n:

        print(f"n --> {cant_datos}\n")

        with open(file_name,"a") as f:

            f.write(f"n --> {cant_datos}\n")
            arr1 = gen_arr(cant_datos )
            arr2 = [] + arr1 

            #Executing the sort 
            timeMerge = timeit(lambda : merge_sort(arr1), number=1)
            timeInsertion = timeit(lambda : insertion_sort(arr2), number=1)

            # print("Array ordenado:", arr)
            f.write(f"Merge Sort Time: {format(timeMerge)} seconds\n")
            print(f"Merge Sort Time: {format(timeMerge)} seconds\n")
            
            f.write(f"Insertion Sort Time: {format(timeInsertion)} seconds\n")
            print(f"Insertion Sort Time: {format(timeInsertion)} seconds\n")


            f.write(f"\n\n")





if __name__ == "__main__":
    main()


