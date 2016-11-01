/*
 * Result for lesson:
 * https://codility.com/programmers/lessons/1-iterations/binary_gap/
 */

function solution(A) {
    var binary = A.toString(2);
    var binaryArray = binary.split("");
    var count = result = 0;
    var start=false;

    for(i=0; i<binaryArray.length; i++){
    	if(binaryArray[i]==="1"){
    		if(count > result){
    			result = count;
    			count = 0;
    		}
    		if(start){
    			count = 0;
    		}else{
    			start = true;
    		}
    	}
    	if(start && binaryArray[i]==="0"){
    		count += 1;
    	}
    }
    return result;
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

test(solution, [9], 2);
test(solution, [529], 4);
test(solution, [20], 1);
test(solution, [15], 0);
test(solution, [1041], 5);
test(solution, [0], 0);
test(solution, [1], 0);
test(solution, [66561], 9);
test(solution, [74901729], 4);
