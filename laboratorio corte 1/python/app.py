from merge_sort import merge_sort 
from timeit import timeit
import numpy as np
from os import path 
from datetime import datetime
import pyperclip

n = [1000,10000,100000,1000000,10000000]
k = 5


def gen_arr(n):
    return [ np.random.random() for _ in range(n) ]

def format(float):
    return str(float).replace(".",",")

def main ():
    times = []
    for cant_datos in n:
        file_name = f"./sets/n_{cant_datos}_sets_{datetime.now().timestamp()}.txt"  

        with open(file_name,"a") as f:
            f.write(f"n --> {cant_datos}\n")

        print(f"n --> {cant_datos}\n")
        for i in range(k):

            with open(file_name, "a") as f:

                progress = f"({i + 1}/{k})"
                
                print(f"\n{progress} Iteracion {i + 1}")
                f.write(f"{progress} Iteracion {i + 1}\n")

                arr = gen_arr(cant_datos )
                
                #Executing the sort 
                time = timeit(lambda : merge_sort(arr), number = 30)

                # print("Array ordenado:", arr)
                times.append(time)
                f.write(f"Timeit time: {format(time)} seconds\n")
                f.write(f"mean accmulated time: {format(sum(times) / len(times))} seconds\n")
                
                print(time,"sec")
            
            mean_time = sum(times) / len(times)
            print("mean Time: ", str(mean_time).replace(".",","))
            with open(file_name, "a" ) as f:
                f.write(f"mean Time for {cant_datos}: " +  str(mean_time).replace(".",",") + "")




if __name__ == "__main__":
    main()

