/**
 * @param {string[]} tokens
 * @return {number}
 */
// 44 Minutes
// Time complexity: O(n)
// Space complexity: O(n)
var evalRPN = function(tokens) {

  const mathItUp = {
    '+': (x, y) => x + y,
    '-': (x, y) => x - y,
    '*': (x, y) => x * y,
    "/": (x, y) => parseInt(x / y) 
  }

  const stack = [];

  for(const token of tokens) {
    // operator found calculate
    if(mathItUp[token]) {
      const first = parseInt(stack.pop());
      const second = parseInt(stack.pop());

      stack.push(mathItUp[token](second, first));

    } else {
      stack.push(token);
    };
  };

  console.log(stack)

  return stack[0];
};

// if else
var evalRPN = function(tokens) {
  const stack = [];

  for(const token of tokens) {
    console.log(stack, 'hahahahahh')

    if(token === "+") {
      stack.push(parseInt(stack.pop()) + parseInt(stack.pop()));

    } else if(token === "-") {
      const a = parseInt(stack.pop());
      const b = parseInt(stack.pop());

      stack.push(b - a);
    } else if(token === "*") {

      stack.push(parseInt(stack.pop()) * parseInt(stack.pop()))
      
    } else if(token === "/") {
      const a = parseInt(stack.pop());
      const b = parseInt(stack.pop());

      stack.push(parseInt(b / a));
      
    } else {
      stack.push(token);
    }

  };

  return stack[0];
};

// switch case
var evalRPN = function(tokens) {
    var stack = [];
    var len = tokens.length;

    for(var i=0; i<len; i++) {
        var num = Number(tokens[i]); 

        if(isNaN(num)) {
            var num2 = stack.pop();
            var num1 = stack.pop();
            var result = 0;

            switch(tokens[i]) {
                case '+':
                result = num1+num2;
                break;

                case '-':
                result = num1-num2;
                break;

                case '*':
                result = num1*num2;
                break;

                case '/':
                default:
                result = Math.trunc(num1/num2);
                break;
            }

            stack.push(result);
        } else {
            stack.push(num);
        }
    }

    return stack[0];
};



// STACK - Because FIRST IN FIRST-OUT fits for this problem because we have to check prev 2 values when operator comes
// Reverse polish notation
// When operator comes from tokens Do calculation on prev 2 elements and add to the stack
  // Do the above step until iteration reaches the end
  // UPDATE SUM 
// RETURN SUM
