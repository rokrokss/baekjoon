function solution(arrangement){
    var result = 0;
    var st = [];
 
    for (var i=0; i < arrangement.length; i++) {
        if (arrangement[i] === '('){
            st.push(arrangement[i]);
        } else {
            st.pop();
            if (arrangement[i-1] === '(') {
                result += st.length;
            } else result +=1;
        }
    }
    return result ;
}

var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split('\n');
console.log(solution(input[0]));

