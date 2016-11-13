/* Result for lesson:
 * https://codility.com/demo/take-sample-test/brackets/
 * author: Iara Ribeiro - 11/13/2016
 */

function solution(S) {
    // write your code in JavaScript (Node.js 6.4.0)
    result = 1;
    stack = new Array();
    for(var i = 0; i< S.length; i++){
        if(S[i] === "{" | S[i] === "(" | S[i] === "["){
            stack.push(S[i]);
        }else{
            element = stack.pop();
            if((element === "{" & S[i] != "}") |
                (element === "[" & S[i] != "]") |
                (element === "(" & S[i] != ")") | 
                (typeof element === 'undefined')){
                    return 0;
            }
        }
    }
    
    if(stack.length > 0){
        return 0;
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

test(solution, ['{[()()]}'], 1);
test(solution, ['([)()]'], 0);
test(solution, [')('], 0);
test(solution, ['{{{{'], 0)