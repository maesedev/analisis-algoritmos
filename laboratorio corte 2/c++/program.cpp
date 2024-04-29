#include <iostream>
#include <fstream>
#include <vector>
#include <ctime>
#include <random>
#include <chrono>
#include <algorithm>

using namespace std;

const vector<int> n = {1000, 10000, 100000, 1000000, 10000000};

vector<double> genArr(int n) {
    random_device rd;
    mt19937 gen(rd());
    uniform_real_distribution<> dis(0.0, 1.0);
    vector<double> arr(n);
    for (int i = 0; i < n; ++i) {
        arr[i] = dis(gen);
    }
    return arr;
}

double format(double num) {
    return round(num * 1000000.0) / 1000000.0; // Rounding to 6 decimal places
}

void quicksort(vector<double>& arr, int low, int high) {
    if (low < high) {
        int pi = low + (high - low) / 2;
        double pivot = arr[pi];
        int i = low, j = high;
        while (i <= j) {
            while (arr[i] < pivot) i++;
            while (arr[j] > pivot) j--;
            if (i <= j) {
                swap(arr[i], arr[j]);
                i++;
                j--;
            }
        }
        if (low < j) quicksort(arr, low, j);
        if (i < high) quicksort(arr, i, high);
    }
}

int partition(vector<double>& arr, int low, int high) {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(low, high);
    int pivotIndex = dis(gen);
    swap(arr[pivotIndex], arr[high]);

    double pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void randQuicksort(vector<double>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        randQuicksort(arr, low, pi - 1);
        randQuicksort(arr, pi + 1, high);
    }
}

int main() {
    string fileName = "./sets/set_" + to_string(time(nullptr)) + ".txt";

    for (int cantDatos : n) {
        cout << "n --> " << cantDatos << endl;

        ofstream outputFile(fileName, ios::app);
        if (!outputFile.is_open()) {
            cerr << "Error opening file: " << fileName << endl;
            return 1;
        }

        outputFile << "n --> " << cantDatos << endl;

        int numeroRepeticiones = cantDatos != 10000000 ? 100 : 10;

        vector<double> quicksortTime(numeroRepeticiones);
        vector<double> randQuicksortTime(numeroRepeticiones);
        for (int i = 0; i < numeroRepeticiones; ++i) {
            cout << i + 1 << " / " << numeroRepeticiones << endl;

            vector<double> arr1 = genArr(cantDatos);
            vector<double> arr2 = arr1;

            cout << "Array generado" << endl;

            auto start = chrono::steady_clock::now();
            quicksort(arr1, 0, arr1.size() - 1);
            auto end = chrono::steady_clock::now();
            quicksortTime[i] = chrono::duration<double>(end - start).count();

            start = chrono::steady_clock::now();
            randQuicksort(arr2, 0, arr2.size() - 1);
            end = chrono::steady_clock::now();
            randQuicksortTime[i] = chrono::duration<double>(end - start).count();
        }

        double averageQuickStime = accumulate(quicksortTime.begin(), quicksortTime.end(), 0.0) / numeroRepeticiones;
        double averageRandQuickStime = accumulate(randQuicksortTime.begin(), randQuicksortTime.end(), 0.0) / numeroRepeticiones;

        outputFile << "Quick Sort average Time: " << format(averageQuickStime) << " seconds" << endl;
        cout << "\nQuick Sort average Time: " << format(averageQuickStime) << " seconds\n";

        outputFile << "Randomized Quick Sort average Time: " << format(averageRandQuickStime) << " seconds" << endl;
        cout << "Randomized Quick Sort average Time: " << format(averageRandQuickStime) << " seconds\n";

        outputFile << "\n\n";
    }

    return 0;
}
