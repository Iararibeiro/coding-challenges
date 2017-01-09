/* Result for lesson:
 * https://codility.com/programmers/lessons/7-stacks_and_queues/fish/
 * author: Iara Ribeiro - 11/13/2016
 */

function solution(A, B) {
    // write your code in JavaScript (Node.js 6.4.0)
    liveFish = new Array();
    actualDirection = B[0];
    liveFish.push(0); 
    lastFish = 0;
    
    for(var i = 1; i < (A.length); i++){
        if(B[lastFish] === 1 && B[i] === 0){
            if(A[lastFish]<A[i]){
                liveFish.pop();
                liveFish.push(i);
                lastFish = i;
            }
        }else{
            liveFish.push(i);
            lastFish = i;
        }
    }
    
    return liveFish.length;   
    
}

function test(functionToTest, args, expected) {
    var result = functionToTest.apply(this, args);
    console.log("Expected " + expected + ", was " + result);
}

test(solution, [[4,3,2,1,5],[0,1,0,0,0]], 2);
test(solution, [[4,3,2,1,5],[0,0,0,0,0]], 5);
test(solution, [[4,3,2,1],[0,1,0,1]], 3);
test(solution, [[4,3,2,1],[1,0,1,0]], 2);