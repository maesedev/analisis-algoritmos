import random

def partition(arr, low, high):
    # Escogemos un pivote aleatorio y lo intercambiamos con el último elemento
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def RandQuicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        
        RandQuicksort(arr, low, pi - 1)
        RandQuicksort(arr, pi + 1, high)


if __name__ == "__main__":

    # Ejemplo de uso
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    RandQuicksort(arr, 0, n-1)
    print("Arreglo ordenado:")
    print(arr)
