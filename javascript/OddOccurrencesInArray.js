
/*
 * @IaraRibeiro
 * Result for lesson:
 * https://codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
 */

function solution(A) {
    // write your code in JavaScript (Node.js 6.4.0)
    var N = A.length;
    var unpaired=0;
    for(var i=0; i<N; i++){
       unpaired = unpaired ^ A[i];
    }
    return unpaired;
}

/*
 * tests
 */

function test(functionToTest, args, expected) {
	var result = functionToTest.apply(this, args);
    if (result !== expected) {
        console.log(args.toString(2));
        console.log("Expected " + expected + ", but was " + result);
    }
}

test(solution, [[9]], 9);
test(solution, [[5,2,5]], 2);
test(solution, [[2,0,2,0,3]], 3);
test(solution, [[1,5,1,5]], 0)