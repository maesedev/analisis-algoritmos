import fs from 'fs';

const n = [1000, 10000, 100000, 1000000, 10000000];

function genArr(n) {
    const arr = [];
    for (let i = 0; i < n; i++) {
        arr.push(Math.random());
    }
    return arr;
}

function format(num) {
    return Math.round(num * 1000000) / 1000000; // Rounding to 6 decimal places
}

function partition(arr, low, high) {
    const pivotIndex = Math.floor(Math.random() * (high - low + 1)) + low;
    [arr[pivotIndex], arr[high]] = [arr[high], arr[pivotIndex]];

    const pivot = arr[high];
    let i = low - 1;
    for (let j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
    }
    [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
    return i + 1;
}

function quicksort(arr, low, high) {
    if (low < high) {
        const pi = partition(arr, low, high);
        quicksort(arr, low, pi - 1);
        quicksort(arr, pi + 1, high);
    }
}

function main() {
    const fileName = `./sets/set_${Math.floor(Date.now() / 1000)}.txt`;

    n.forEach(cantDatos => {
        console.log(`n --> ${cantDatos}\n`);
        fs.appendFileSync(fileName, `n --> ${cantDatos}\n`);

        const numeroRepeticiones = cantDatos !== 10000000 ? 100 : 10;

        const quicksortTime = [];
        const randQuicksortTime = [];
        for (let i = 0; i < numeroRepeticiones; i++) {
            console.log(`${i + 1} / ${numeroRepeticiones}`);

            const arr1 = genArr(cantDatos);
            const arr2 = [...arr1];

            console.log("Array generado");

            const startQuicksort = process.hrtime.bigint();
            quicksort(arr1, 0, arr1.length - 1);
            const endQuicksort = process.hrtime.bigint();
            quicksortTime.push(Number(endQuicksort - startQuicksort) / 1e9);

            const startRandQuicksort = process.hrtime.bigint();
            arr2.sort((a, b) => a - b); // Sort for comparison with random quicksort
            const endRandQuicksort = process.hrtime.bigint();
            randQuicksortTime.push(Number(endRandQuicksort - startRandQuicksort) / 1e9);
        }

        const averageQuickStime = quicksortTime.reduce((acc, curr) => acc + curr, 0) / numeroRepeticiones;
        const averageRandQuickStime = randQuicksortTime.reduce((acc, curr) => acc + curr, 0) / numeroRepeticiones;

        fs.appendFileSync(fileName, `Quick Sort average Time: ${format(averageQuickStime)} seconds\n`);
        console.log(`\nQuick Sort average Time: ${format(averageQuickStime)} seconds\n`);

        fs.appendFileSync(fileName, `Randomized Quick Sort average Time: ${format(averageRandQuickStime)} seconds\n`);
        console.log(`Randomized Quick Sort average Time: ${format(averageRandQuickStime)} seconds\n`);

        fs.appendFileSync(fileName, '\n\n');
    });
}

main();
