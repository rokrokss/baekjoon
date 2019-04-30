function heapify(arr, idx, heapSize) {
  let largest = idx;
  let left = 2 * idx + 1;
  let right = 2 * idx + 2;
  if (left < heapSize && arr[left] > arr[largest]) {
    largest = left;
  }
  if (right < heapSize && arr[right] > arr[largest]) {
    largest = right;
  }
  if (largest !== idx) {
    [arr[largest], arr[idx]] = [arr[idx], arr[largest]];
    heapify(arr, largest, heapSize);
  }
}


function heapsort(arr) {
  for (let i = parseInt((arr.length - 1) / 2); i >= 0; i--) {
    heapify(arr, i, arr.length);
  }
  for (let i = arr.length - 1; i > 0; i--) {
    [arr[i], arr[0]] = [arr[0], arr[i]];
    heapify(arr, 0, i);
  }
}


let arr = [2, 342, 12, 531, 2, 3, 1, 62, 10];
console.log(arr);
heapsort(arr);
console.log(arr);

