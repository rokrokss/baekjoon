function getMaxH(arr, n) {
  let max = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (arr[i][j] > max) {
        max = arr[i][j];
      }
    }
  }
  return max;
}


function visit(arr, n, h, x, y, visited, directions) {
  if (x < 0 || y < 0 || x >= n || y >= n) {
    return;
  }
  if (arr[x][y] <= h || visited[x][y]) {
    return;
  }
  visited[x][y] = true;
  for (let i = 0; i < directions.length; i++) {
    visit(arr, n, h, x + directions[i][0], y + directions[i][1], visited, directions);
  }
}


let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const n = parseInt(input.shift());
input = input.map(x => {return x.split(' ').map(y => {return parseInt(y);});});
let ans = 1;
let maxH = getMaxH(input, n);
let visited = Array(n);
const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];
for (let i = 0; i < n; i++) {
  visited[i] = Array(n);
}
for (let i = 1; i <= maxH; i++) {
  for (let j = 0; j < n; j++) {
    for (let k = 0; k < n; k++) {
      visited[j][k] = false;
    }
  }
  let cnt = 0;
  for (let j = 0; j < n; j++) {
    for (let k = 0; k < n; k++) {
      if (visited[j][k] || input[j][k] <= i) {
        continue;
      }
      visit(input, n, i, j, k, visited, directions)
      cnt++;
    }
  }
  if (cnt > ans) {
    ans = cnt;
  }
}
console.log(ans);

