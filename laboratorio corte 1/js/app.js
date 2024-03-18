import mergeSort from "./mergeSort.js"
import insertionSort from "./insertionSort.js"
import { performance } from "perf_hooks";
import fs from "fs"

const n = [1000, 10000, 100000, 1000000, 10000000];

function genArr(n) {
    const arr = [];
    for (let i = 0; i < n; i++) {
        arr.push(Math.random());
    }
    return arr;
}

function format(float) {
    return float.toString().replace(".", ",");
}

function main() {
    const fileName = `./sets/merge_set_${Date.now()}.txt`;

    n.forEach(cantDatos => {
        console.log(`n --> ${cantDatos}\n`);

        fs.appendFileSync(fileName, `n --> ${cantDatos}\n`);

        const arr1 = genArr(cantDatos);
        const arr2 = [...arr1];

        const startTimeMerge = performance.now();
        mergeSort(arr1);
        const endTimeMerge = performance.now();
        const timeMerge = (endTimeMerge - startTimeMerge) / 1000;

        // const startTimeInsertion = performance.now();
        // insertionSort(arr2);
        // const endTimeInsertion = performance.now();
        // const timeInsertion = (endTimeInsertion - startTimeInsertion) / 1000;

        fs.appendFileSync(fileName, `Merge Sort Time: ${format(timeMerge)} seconds\n`);
        console.log(`Merge Sort Time: ${format(timeMerge)} seconds\n`);

        // fs.appendFileSync(fileName, `Insertion Sort Time: ${format(timeInsertion)} seconds\n`);
        // console.log(`Insertion Sort Time: ${format(timeInsertion)} seconds\n`);

        fs.appendFileSync(fileName, `\n\n`);
    });
}

main();
