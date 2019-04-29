function randomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}


function _quickSort(arr, start, end) {
  if (start >= end) {
    return;
  }
  let pivot_idx = randomInt(start, end);
  let pivot_val = arr[pivot_idx];
  [arr[pivot_idx], arr[end]] = [arr[end], arr[pivot_idx]];
  let store_idx = start;
  for (let i = start; i < end; i++) {
    if (arr[i] < pivot_val) {
      [arr[store_idx], arr[i]] = [arr[i], arr[store_idx]];
      store_idx++;
    }
  }
  [arr[store_idx], arr[end]] = [arr[end], arr[store_idx]];
  _quickSort(arr, start, store_idx - 1);
  _quickSort(arr, store_idx + 1, end);
}


function quickSort(arr) {
  return _quickSort(arr, 0, arr.length - 1);
}

a = [1, 2134, 123, 23, 42, 555, 22, 52, 3, 5, 2, 99];
console.log(a);
quickSort(a);
console.log(a);

