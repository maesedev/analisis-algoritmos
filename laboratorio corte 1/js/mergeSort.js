
export default function mergeSort(arr) {
    if (arr.length <= 1) {
        return arr;
    }

    const mid = Math.floor(arr.length / 2);
    const leftHalf = arr.slice(0, mid);
    const rightHalf = arr.slice(mid);

    return merge(mergeSort(leftHalf), mergeSort(rightHalf));
}

function merge(leftHalf, rightHalf) {
    let result = [];
    let leftIndex = 0;
    let rightIndex = 0;

    while (leftIndex < leftHalf.length && rightIndex < rightHalf.length) {
        if (leftHalf[leftIndex] < rightHalf[rightIndex]) {
            result.push(leftHalf[leftIndex]);
            leftIndex++;
        } else {
            result.push(rightHalf[rightIndex]);
            rightIndex++;
        }
    }

    return result.concat(leftHalf.slice(leftIndex)).concat(rightHalf.slice(rightIndex));
}

