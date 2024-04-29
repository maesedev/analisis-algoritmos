import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Random;

public class Program {
    static final int[] n = { 1000, 10000, 100000, 1000000, 10000000 };

    static double[] genArr(int n) {
        Random rnd = new Random();
        double[] arr = new double[n];
        for (int i = 0; i < n; i++) {
            arr[i] = rnd.nextDouble();
        }
        return arr;
    }

    static double format(double num) {
        return Math.round(num * 1000000.0) / 1000000.0; // Rounding to 6 decimal places
    }

    public static void main(String[] args) {
        String fileName = String.format("./sets/set_%d.txt", System.currentTimeMillis() / 1000);

        for (int cantDatos : n) {
            System.out.println("n --> " + cantDatos + "\n");

            try (PrintWriter writer = new PrintWriter(new FileWriter(fileName, true))) {
                writer.println("n --> " + cantDatos);

                int numeroRepeticiones = cantDatos != 10000000 ? 100 : 10;

                double[] quicksortTime = new double[numeroRepeticiones];
                double[] randQuicksortTime = new double[numeroRepeticiones];
                for (int i = 0; i < numeroRepeticiones; i++) {
                    System.out.println((i + 1) + " / " + numeroRepeticiones);

                    double[] arr1 = genArr(cantDatos);
                    double[] arr2 = arr1.clone();

                    System.out.println("Array generado");

                    // Executing the sort
                    long startTime = System.nanoTime();
                    quicksort(arr1, 0, arr1.length - 1);
                    quicksortTime[i] = (System.nanoTime() - startTime) / 1e9;

                    startTime = System.nanoTime();
                    randQuicksort(arr2, 0, arr2.length - 1);
                    randQuicksortTime[i] = (System.nanoTime() - startTime) / 1e9;
                }

                double averageQuickStime = 0;
                for (double time : quicksortTime) {
                    averageQuickStime += time;
                }
                averageQuickStime /= numeroRepeticiones;

                double averageRandQuickStime = 0;
                for (double time : randQuicksortTime) {
                    averageRandQuickStime += time;
                }
                averageRandQuickStime /= numeroRepeticiones;

                writer.println("Quick Sort average Time: " + format(averageQuickStime) + " seconds");
                System.out.println("\n\nQuick Sort average Time: " + format(averageQuickStime) + " seconds\n");

                writer.println("Randomized Quick Sort average Time: " + format(averageRandQuickStime) + " seconds");
                System.out.println("Randomized Quick Sort average Time: " + format(averageRandQuickStime) + " seconds\n");

                writer.println("\n\n");
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    static int partition(double[] arr, int low, int high) {
        Random rnd = new Random();
        int pivotIndex = rnd.nextInt(high - low + 1) + low;
        swap(arr, pivotIndex, high);

        double pivot = arr[high];
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        swap(arr, i + 1, high);
        return i + 1;
    }

    static void quicksort(double[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quicksort(arr, low, pi - 1);
            quicksort(arr, pi + 1, high);
        }
    }

    static void swap(double[] arr, int i, int j) {
        double temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    static void randQuicksort(double[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            randQuicksort(arr, low, pi - 1);
            randQuicksort(arr, pi + 1, high);
        }
    }
}
