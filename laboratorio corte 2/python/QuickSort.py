def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == "__main__":

    # Ejemplo de uso
    arr = [3, 6, 8, 10, 1, 2, 1]
    print("Arreglo original:", arr)
    sorted_arr = quicksort(arr)
    print("Arreglo ordenado:", sorted_arr)
