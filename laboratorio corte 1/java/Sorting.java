/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Sorting;


import java.io.FileWriter;
import java.io.IOException;
import java.time.Instant;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class Sorting {

    // Merge Sort implementation
    private static void merge(double[] arr, int l, int m, int r) {
        int n1 = m - l + 1;
        int n2 = r - m;

        double[] L = Arrays.copyOfRange(arr, l, m + 1);
        double[] R = Arrays.copyOfRange(arr, m + 1, r + 1);

        int i = 0, j = 0, k = l;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    private static void mergeSort(double[] arr, int l, int r) {
        if (l < r) {
            int m = l + (r - l) / 2;
            mergeSort(arr, l, m);
            mergeSort(arr, m + 1, r);
            merge(arr, l, m, r);
        }
    }

    // Insertion Sort implementation
    private static void insertionSort(double[] arr) {
        int n = arr.length;
        for (int i = 1; i < n; ++i) {
            double key = arr[i];
            int j = i - 1;

            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
    }

    private static double[] generateArray(int n) {
        double[] arr = new double[n];
        Random random = new Random();
        for (int i = 0; i < n; i++) {
            arr[i] = random.nextDouble();
        }
        return arr;
    }

    private static String format(double num) {
        return String.format("%.9f", num);
    }

    public static void main(String[] args) throws IOException {
        List<Integer> n = Arrays.asList(1000, 10000, 100000, 1000000, 10000000);
        String fileName = "C:\\Users\\Santiago\\Desktop\\maese dev\\1. Estudio\\Trabajos universidad\\4 - Cuarto Semestre\\Analisis de algoritmos\\laboratorio\\laboratorio corte 1\\java\\sets\\insertion_set_" + Instant.now().getEpochSecond() + ".txt";

        for (int cantDatos : n) {
            System.out.println("n --> " + cantDatos);

            try (FileWriter fileWriter = new FileWriter(fileName, true)) {
                fileWriter.write("n --> " + cantDatos + "\n");
                fileWriter.close();
            }

            double[] arr1 = generateArray(cantDatos);
            double[] arr2 = Arrays.copyOf(arr1, arr1.length);
/*
            long startTimeMerge = System.nanoTime();
            mergeSort(arr1, 0, arr1.length - 1);
            long endTimeMerge = System.nanoTime();
            double timeMerge = (endTimeMerge - startTimeMerge) / 1e9;
*/
            long startTimeInsertion = System.nanoTime();
            insertionSort(arr2);
            long endTimeInsertion = System.nanoTime();
            double timeInsertion = (endTimeInsertion - startTimeInsertion) / 1e9;
            
            try (FileWriter fileWriter = new FileWriter(fileName, true)) {
                //fileWriter.write("Merge Sort Time: " + format(timeMerge) + " seconds\n");
                fileWriter.write("Insertion Sort Time: " + format(timeInsertion) + " seconds\n\n\n");
                fileWriter.close();
            }

            //System.out.println("Merge Sort Time: " + format(timeMerge) + " seconds");
            System.out.println("Insertion Sort Time: " + format(timeInsertion) + " seconds\n");
        }
    }
}
