/* Result for lesson:
 * https://codility.com/demo/take-sample-test/tape_equilibrium
 */

function solution(A) {
   var sumAfter = sumBefore = 0;
    var minDiff = Number.POSITIVE_INFINITY;
     
    A.forEach(function(value){
        sumAfter += value;
    });
     
    for (var i = 1; i < A.length; i++){
        sumBefore += A[i -1];
        sumAfter = sumAfter - A[i -1];
        minDiffTemp = Math.abs(sumBefore - sumAfter);
        if (minDiffTemp < minDiff){
            minDiff = minDiffTemp;
        }
    }
    return minDiff;
}
/*
 * tests
 */

function test(functionToTest, args, expected) {
	var result = functionToTest.apply(this, args);
    console.log("Expected " + expected + ", was " + result);
}

test(solution, [[3,1,2,4,3]], 1);
//test(solution, [[5,2,5],1], [5,5,2]);
//test(solution, [[2,0,2,0,3],3], [0,3,2,0,2]);
//test(solution, [[1,5,1,5],0], [1,5,1,5])