/*
This algorithm implements a generic version of a Stack in javascript, the idea
with the algorithm in this directory is have a source for future reference in
problems from codility or similar sites/problems.

The algorithm used the theory presented in Introduction to Algorithms, 
a book by Thomas H. Cormen.

@author: Iara Ribeiro - 11/12/2016.
*/
var head = tail = 0;
var Q = [];

function queueEmpty(Q){
	if(head === 0){
		return true;
	}
	return false;
}

function enqueue(Q,x){
	Q[tail] = x;
	if(tail === Q.length){
		tail = 1;
	}else{
		tail += 1;
	}
}

function dequeue(Q){
	x = Q[head];
	if(head === Q.length){
		head = 1;
	}else{
		head += 1;
	}
	return x;
}

function print(Q){
	var result = "[";
	for(var i = head; i < tail; i++){
		if( (tail - i) == 1){
			result += Q[i];
		}else{
			result = result + Q[i] + ",";
		}
	}
	return result+"]";
}

function test(functionToTest, args, expected) {
	var result = functionToTest.apply(this, args);
    console.log("Expected " + expected + ", was " + result);
}

test(queueEmpty, Q, true);
enqueue(Q,"banana");
test(print, [Q], "[banana]");
enqueue(Q,"apple");
test(print, [Q], "[banana,apple]");
dequeue(Q);
test(print, [Q], "[apple]");
enqueue(Q,"pineapple");
test(print, [Q], "[apple,pineapple]");
dequeue(Q);
dequeue(Q);
test(print, [Q], "[]");