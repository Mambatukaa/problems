// Time Complexity: O(n)
// Space Complexity: O(n)
const fib = (n) => {
  if(n < 2) {
    return 0;
  }

  if(n < 3) {
    return 1;
  }


  return fib(n - 1) + fib(n - 2);
}


console.log(fib(6));
