using System;
using System.IO;
using System.Linq;

public class Program
{
    static readonly int[] n = { 1000, 10000, 100000, 1000000, 10000000 };

    static double[] GenArr(int n)
    {
        Random rnd = new Random();
        double[] arr = new double[n];
        for (int i = 0; i < n; i++)
        {
            arr[i] = rnd.NextDouble();
        }
        return arr;
    }

    static double Format(double num)
    {
        return Math.Round(num, 6); // Rounding to 6 decimal places
    }

    static void Main(string[] args)
    {
        string fileName = $"./sets/set_{DateTimeOffset.Now.ToUnixTimeSeconds()}.txt";

        foreach (int cantDatos in n)
        {
            Console.WriteLine($"n --> {cantDatos}\n");

            using (StreamWriter sw = File.AppendText(fileName))
            {
                sw.WriteLine($"n --> {cantDatos}");

                int numeroRepeticiones = cantDatos != 10000000 ? 100 : 10;

                double[] quicksortTime = new double[numeroRepeticiones];
                double[] randQuicksortTime = new double[numeroRepeticiones];
                for (int i = 0; i < numeroRepeticiones; i++)
                {
                    Console.WriteLine($"{i + 1} / {numeroRepeticiones}");

                    double[] arr1 = GenArr(cantDatos);
                    double[] arr2 = arr1.ToArray();

                    Console.WriteLine("Array generado");

                    // Executing the sort
                    var watch = System.Diagnostics.Stopwatch.StartNew();
                    QuickSort(arr1, 0, arr1.Length - 1);
                    watch.Stop();
                    quicksortTime[i] = watch.Elapsed.TotalSeconds;

                    watch = System.Diagnostics.Stopwatch.StartNew();
                    RandQuickSort(arr2, 0, arr2.Length - 1);
                    watch.Stop();
                    randQuicksortTime[i] = watch.Elapsed.TotalSeconds;
                }

                double averageQuickStime = quicksortTime.Sum() / numeroRepeticiones;
                double averageRandQuickStime = randQuicksortTime.Sum() / numeroRepeticiones;

                sw.WriteLine($"Quick Sort average Time: {Format(averageQuickStime)} seconds");
                Console.WriteLine($"\n\nQuick Sort average Time: {Format(averageQuickStime)} seconds\n");

                sw.WriteLine($"Randomized Quick Sort average Time: {Format(averageRandQuickStime)} seconds");
                Console.WriteLine($"Randomized Quick Sort average Time: {Format(averageRandQuickStime)} seconds\n");

                sw.WriteLine("\n\n");
            }
        }
    }

    static int Partition(double[] arr, int low, int high)
    {
        Random rnd = new Random();
        int pivotIndex = rnd.Next(low, high);
        Swap(arr, pivotIndex, high);

        double pivot = arr[high];
        int i = low - 1;
        
        for (int j = low; j < high; j++)
        {
            if (arr[j] < pivot)
            {
                i++;
                Swap(arr, i, j);
            }
        }

        Swap(arr, i + 1, high);
        return i + 1;
    }

    static void QuickSort(double[] arr, int low, int high)
    {
        if (low < high)
        {
            int pi = Partition(arr, low, high);
            QuickSort(arr, low, pi - 1);
            QuickSort(arr, pi + 1, high);
        }
    }

    static void Swap(double[] arr, int i, int j)
    {
        double temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    static void RandQuickSort(double[] arr, int low, int high)
    {
        if (low < high)
        {
            int pi = Partition(arr, low, high);
            RandQuickSort(arr, low, pi - 1);
            RandQuickSort(arr, pi + 1, high);
        }
    }
}
