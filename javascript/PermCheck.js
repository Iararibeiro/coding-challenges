/* Result for lesson:
 * https://codility.com/programmers/lessons/4-counting_elements/perm_check/
 */

function solution(A) {
    // write your code in JavaScript (Node.js 6.4.0)
    A = A.sort();
    var result = 1;
    
    for(var i = 0; i < (A.length-1); i++){
        if((A[i+1] - A[i])!=1){
            result = 0;
        }
    }
    return result;
}
/*
 * tests
 */

function test(functionToTest, args, expected) {
	var result = functionToTest.apply(this, args);
    console.log("Expected " + expected + ", was " + result);
}

test(solution, [[3,1,2,4,3]], 0);
test(solution, [[1,2,3]], 1);
test(solution, [[0,1,1,2]], 0);
test(solution, [[1]], 1)