from QuickSort import quicksort
from RandQuickSort import RandQuicksort
from timeit import timeit
import numpy as np
from datetime import datetime

n = [10000000]


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
            
            numeroRepeticiones = 100 if cant_datos != 10000000 else 10

            quicksortTime = []
            RandQuicksortTime = []
            for i in range(numeroRepeticiones):

                print(f"{i + 1} / {numeroRepeticiones}")

                arr1 = gen_arr(cant_datos)
                arr2 = [] + arr1 
                print(f"Array generado")
                #Executing the sort 
                quicksortTime.append(timeit(lambda :quicksort( arr1 ) , number=1 ))
                RandQuicksortTime.append(timeit(lambda :RandQuicksort( arr2 , 0 , numeroRepeticiones - 1 ) , number=1 ))



            averageQuickStime = sum(quicksortTime) / numeroRepeticiones
            averageRandQuickStime = sum(RandQuicksortTime) / numeroRepeticiones

            # print("Array ordenado:", arr)
            f.write(f"Quick Sort average Time: {format( averageQuickStime )} seconds\n")
            print(f"\n\nQuick Sort average Time: {format( averageQuickStime )} seconds\n")
            
            
            f.write(f"Randomized Quick Sort average  Time: {format( averageRandQuickStime )} seconds\n")
            print(f"Randomized Quick Sort average Time: {format( averageRandQuickStime )} seconds\n")


            f.write(f"\n\n")





if __name__ == "__main__":
    main()


