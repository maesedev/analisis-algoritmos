
import fs from "fs"
import mergeSort from "./mergeSort.js"
import insertionSort from "./insertionSort.js"
import { performance } from 'perf_hooks';

const n = [1000, 10000, 100000, 1000000, 10000000];
const k = 5;




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
    const times = [];
    n.forEach(cant_datos => {
        const file_name = `./sets/n_${cant_datos}_sets_${Date.now()}.txt`;

        fs.appendFileSync(file_name, `n --> ${cant_datos}\n`);
        console.log(`n --> ${cant_datos}\n`);

        for (let i = 0; i < k; i++) {
            const progress = `(${i + 1}/${k})`;

            console.log(`\n${progress} Iteracion ${i + 1}`);
            fs.appendFileSync(file_name, `${progress} Iteracion ${i + 1}\n`);

            const arr = genArr(cant_datos);

            const startTime = performance.now();
            mergeSort(arr);
            const endTime = performance.now();
            const time = (endTime - startTime) / 1000; // convert to seconds

            times.push(time);
            fs.appendFileSync(file_name, `Timeit time: ${format(time)} seconds\n`);
            fs.appendFileSync(file_name, `mean accmulated time: ${format(times.reduce((acc, cur) => acc + cur, 0) / times.length)} seconds\n`);

            console.log(time.toFixed(6), "sec");
        }

        const meanTime = times.reduce((acc, cur) => acc + cur, 0) / times.length;
        console.log("mean Time: ", meanTime.toFixed(6));

        fs.appendFileSync(file_name, `\n\nmean Time for ${cant_datos}: ${meanTime.toFixed(6)}\n`);
    });
}

main();

