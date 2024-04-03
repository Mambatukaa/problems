// iterative


// Time Complexity: O(n)
// Space Complexity: O(n)
const fib = (n) => {
  const dp = new Array(n + 1).fill(0);

  dp[1] = 1;

  for(let i = 2; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }

  console.log(dp)

  return dp[n];
};

// Time Complexity: O(2^n)
// Space Complexity: O(2^n)
const fibonacci = (n) => {
  if(n === 1) {
    return 1;
  };

  if(n === 0) {
    return 0;
  };


  return fibonacci(n - 1) + fibonacci(n - 2);
};

// Time Complexity: O(n)
// Space Complexity: O(n)

const memo = new Map();

const fibonacciWithMemo = (n) => {
  if(n === 1) {
    return 1;
  };

  if(n === 0) {
    return 0;
  };


  if(memo.has(n)) {
    return memo.get(n)
  };

  memo.set(n, fibonacciWithMemo(n - 1) + fibonacciWithMemo(n - 2));

  return memo.get(n);
};


/*
 
fibonacci(5);
  fibonacci(4) + fibonacci(3);
    fibonacci(3) + fibonacci(2)
      fibonacci(2) + fibonacci(1)
      fibonacci(1) + fibonacci(0)
    fibonacci(2) + fibonacci(1)





 
 */
