const isSetMemo = Array(201);
const isListMemo = Array(201);
for (let i = 0; i < 201; i++) {
  isSetMemo[i] = Array(201);
  isListMemo[i] = Array(201);
}


function isElem(str, start, end) {
  if (end - start === 0)
    return 1;
  return isSet(str, start, end);
}


function isList(str, start, end) {
  if (isListMemo[start][end] != -1)
    return isListMemo[start][end];
  if (isElem(str, start, end))
    return (isListMemo[start][end] = 1);
  for (let i = start + 1; i < end; i++)
    if (str[i] == ',' && isElem(str, start, i - 1) && isList(str, i + 1, end))
      return (isListMemo[start][end] = 1);
  return (isListMemo[start][end] = 0);
}


function isSet(str, start, end) {
  if (isSetMemo[start][end] != -1)
    return isSetMemo[start][end];
  if (end < start)
    return (isSetMemo[start][end] = 1);
  if (str[start] != '{' || str[end] != '}')
    return (isSetMemo[start][end] = 0);
  return (isSetMemo[start][end] = isList(str, start + 1, end - 1));
}


let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const t = parseInt(input[0]);
for (let i = 1; i <= t; i++) {
  for (let j = 0; j < 201; j++) {
    for (let k = 0; k < 201; k++) {
      isSetMemo[j][k] = -1;
      isListMemo[j][k] = -1;
    }
  }
  const set = isSet(input[i], 0, input[i].length - 1);
  console.log(`Word #${i}: ${set ? "Set" : "No Set"}`);
}

