/* You are given an integer m (1 ¬ m ¬ 1 000 000) and two non-empty, zero-indexed
arrays A and B of n integers, a 0 , a 1 , . . . , a n−1 and b 0 , b 1 , . . . , b n−1 respectively (0 ¬ a i , b i ¬ m).
The goal is to check whether there is a swap operation which can be performed on these
arrays in such a way that the sum of elements in array A equals the sum of elements in
array B after the swap. By swap operation we mean picking one element from array A and
one element from array B and exchanging them.
*/

function solution(A,B) {
    // write your code in JavaScript (Node.js 6.4.0)
    var sumA=sumB=result=diff = 0;
    var auxA,auxB;

    A.forEach(function(value){sumA += value;});
    B.forEach(function(value){sumB += value;});

    auxA = sumA;
    auxB = sumB;

    for(var i = 0; i<A.length; i++){
    	
    	for(var j=0; j<B.length; j++){
    		diff = B[j] - A[i];

    		auxA = auxA + diff;
    		auxB = auxB - diff;

    		if(auxA === auxB){
    			result = auxA;
    		}else{
    			auxA = auxA - diff;
    			auxB = auxB + diff;
    		}
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

test(solution, [[3,1,2],[2,2,0]], 5);
