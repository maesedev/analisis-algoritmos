package main

import (
    "fmt"
    "math/rand"
    "os"
    "time"
)

var n = []int{1000, 10000, 100000, 1000000, 10000000}

func genArr(n int) []float64 {
    arr := make([]float64, n)
    rand.Seed(time.Now().UnixNano())
    for i := 0; i < n; i++ {
        arr[i] = rand.Float64()
    }
    return arr
}

func format(num float64) string {
    return fmt.Sprintf("%.6f", num)
}

func partition(arr []float64, low, high int) int {
    pivotIndex := rand.Intn(high-low+1) + low
    arr[pivotIndex], arr[high] = arr[high], arr[pivotIndex]

    pivot := arr[high]
    i := low - 1
    for j := low; j < high; j++ {
        if arr[j] < pivot {
            i++
            arr[i], arr[j] = arr[j], arr[i]
        }
    }
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1
}

func quicksort(arr []float64, low, high int) {
    if low < high {
        pi := partition(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)
    }
}

func main() {
    fileName := fmt.Sprintf("./sets/set_%d.txt", time.Now().Unix())

    for _, cantDatos := range n {
        fmt.Printf("n --> %d\n\n", cantDatos)

        f, err := os.OpenFile(fileName, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
        if err != nil {
            fmt.Printf("Error opening file: %v\n", err)
            return
        }
        defer f.Close()

        _, err = f.WriteString(fmt.Sprintf("n --> %d\n", cantDatos))
        if err != nil {
            fmt.Printf("Error writing to file: %v\n", err)
            return
        }

        numeroRepeticiones := 100
        if cantDatos == 10000000 {
            numeroRepeticiones = 10
        }

        var quicksortTimeTotal float64
        var randQuicksortTimeTotal float64
        for i := 0; i < numeroRepeticiones; i++ {
            fmt.Printf("%d / %d\n", i+1, numeroRepeticiones)

            arr1 := genArr(cantDatos)
            arr2 := make([]float64, len(arr1))
            copy(arr2, arr1)

            fmt.Println("Array generado")

            start := time.Now()
            quicksort(arr1, 0, len(arr1)-1)
            quicksortTimeTotal += time.Since(start).Seconds()

            start = time.Now()
            quicksort(arr2, 0, len(arr2)-1)
            randQuicksortTimeTotal += time.Since(start).Seconds()
        }

        _, err = f.WriteString(fmt.Sprintf("Quick Sort total Time: %s seconds\n", format(quicksortTimeTotal)))
        if err != nil {
            fmt.Printf("Error writing to file: %v\n", err)
            return
        }
        fmt.Printf("\nQuick Sort total Time: %s seconds\n", format(quicksortTimeTotal))

        _, err = f.WriteString(fmt.Sprintf("Randomized Quick Sort total Time: %s seconds\n\n\n", format(randQuicksortTimeTotal)))
        if err != nil {
            fmt.Printf("Error writing to file: %v\n", err)
            return
        }
        fmt.Printf("Randomized Quick Sort total Time: %s seconds\n\n", format(randQuicksortTimeTotal))
    }
}
