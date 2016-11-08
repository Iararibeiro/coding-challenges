
function solution(X,A) {
    // write your code in JavaScript (Node.js 6.4.0)
    var positions = {};
    var leaves = 0;

    for(var i = 0; i < A.length; i++) {
        if(A[i] <= X && positions[A[i]] !== true) {
            positions[A[i]] = true;
            leaves++;
            if(leaves === X) {
                return i;
            }
        }
    }
    return -1;
}
/*
 * tests
 */

function test(functionToTest, args, expected) {
    var result = functionToTest.apply(this, args);
    console.log("Expected " + expected + ", was " + result);
}

test(solution, [3,[5]], -1);
test(solution, [2,[2,2,2,2,2]], -1);
test(solution, [3,[1,2,3]], 2);