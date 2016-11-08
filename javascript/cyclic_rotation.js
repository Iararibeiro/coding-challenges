/* Result for lesson:
 * https://codility.com/programmers/lessons/2-arrays/cyclic_rotation/
 */

function solution(A,K) {
    // write your code in JavaScript (Node.js 6.4.0)
    var temp = [];
    var newIndex = 0;

    for(var i=0;i<A.length;i++){        
        if(K+i < A.length){
            temp[K+i] = A[i];
        }else{
            newIndex = (K+i)-A.length; 
            temp[newIndex] = A[i];
        }
    }

    return temp;
}

/*
 * tests
 */

function test(functionToTest, args, expected) {
	var result = functionToTest.apply(this, args);
    if (result !== expected) {
        //console.log(args.toString(2));
        console.log("Expected " + expected + ", but was " + result);
    }
}

test(solution, [[9,3],3], [3,9]);
//test(solution, [[5,2,5],1], [5,5,2]);
//test(solution, [[2,0,2,0,3],3], [0,3,2,0,2]);
//test(solution, [[1,5,1,5],0], [1,5,1,5])