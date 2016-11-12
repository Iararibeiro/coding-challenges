/*
This algorithm implements a generic version of a Stack in javascript, the idea
with the algorithm in this directory is have a source for future reference in
problems from codility or similar sites/problems.

The algorithm used the theory presented in Introduction to Algorithms, 
a book by Thomas H. Cormen.

@author: Iara Ribeiro - 11/12/2016.
*/
var top = 0;
var S = [];

function stackEmpty(S){
	if(top === 0){
		return true;
	}
	return false;
}

function push(S,x){
	top += 1;
	S[top] = x;
}

function pop(S){
	if(stackEmpty(S)){
		return "stack empty";
	}else{
		top -= 1;
		return S[top + 1];
	}
}

function print(S){
	var result = "[";
	for(var i = 1; i <= top; i++){
		if( i === 1){
			result += S[i];
		}else{
			result = result + "," + S[i];
		}
	}
	return result+"]";
}

function test(functionToTest, args, expected) {
	var result = functionToTest.apply(this, args);
    console.log("Expected " + expected + ", was " + result);
}

test(stackEmpty, S, true);
push(S,"banana");
test(print, [S], "[banana]");
push(S,"apple");
test(print, [S], "[banana,apple]");
pop(S);
test(print, [S], "[banana]");
push(S,"pineapple");
test(print, [S], "[banana,pineapple]");
pop(S);
test(print, [S], "[]");