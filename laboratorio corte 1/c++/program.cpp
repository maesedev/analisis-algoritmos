#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <ctime>
#include <random>

// Merge Sort implementation
void merge(std::vector<double>& arr, int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;

    std::vector<double> L(n1), R(n2);

    for (int i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

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

void mergeSort(std::vector<double>& arr, int l, int r) {
    if (l >= r)
        return;

    int m = l + (r - l) / 2;
    mergeSort(arr, l, m);
    mergeSort(arr, m + 1, r);
    merge(arr, l, m, r);
}

// Insertion Sort implementation
void insertionSort(std::vector<double>& arr) {
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        double key = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

std::vector<double> generateArray(int n) {
    std::vector<double> arr;
    arr.reserve(n);
    std::default_random_engine generator;
    std::uniform_real_distribution<double> distribution(0.0, 1.0);
    for (int i = 0; i < n; ++i) {
        arr.push_back(distribution(generator));
    }
    return arr;
}

std::string format(double num) {
    return std::to_string(num);
}

int main() {
    std::vector<int> n = {1000, 10000, 100000, 1000000, 10000000};
    std::string file_name = "./sets/insertion_set_1.txt";

    for (int cant_datos : n) {
        std::cout << "n --> " << cant_datos << "\n";

        std::ofstream file(file_name, std::ios::app);
        if (file.is_open()) {
            file << "n --> " << cant_datos << "\n";
        }

        std::vector<double> arr1 = generateArray(cant_datos);
        std::vector<double> arr2(arr1);

        // auto startMerge = std::chrono::high_resolution_clock::now();
        // mergeSort(arr1, 0, arr1.size() - 1);
        // auto endMerge = std::chrono::high_resolution_clock::now();
        // std::chrono::duration<double> elapsedMerge = endMerge - startMerge;

        auto startInsertion = std::chrono::high_resolution_clock::now();
        insertionSort(arr2);
        auto endInsertion = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> elapsedInsertion = endInsertion - startInsertion;

        if (file.is_open()) {
            // file << "Merge Sort Time: " << format(elapsedMerge.count()) << " seconds\n";
            file << "Insertion Sort Time: " << format(elapsedInsertion.count()) << " seconds\n\n\n";
            file.close();
        }

        // std::cout << "Merge Sort Time: " << format(elapsedMerge.count()) << " seconds\n";
        std::cout << "Insertion Sort Time: " << format(elapsedInsertion.count()) << " seconds\n\n";
        file.close();
    }

    return 0;
}
