var input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
var caseNum = input.shift();

for(var i = 0; i < caseNum; i++){
    var inputArr = input[i].split(" ");
    var multifly = parseInt(inputArr[0]);
    var orgStr = inputArr[1];
    var newStr = "";
    for(var j = 0; j < orgStr.length; j++){
        for(var k = 0; k < multifly; k++){
            newStr += orgStr[j];
        }
    }
    console.log("%s", newStr);
}


