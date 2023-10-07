// Time Complexity: O(n)
// Space Complexity: O(n)
const fib = (n) => {
  if(n === 2) {
    return 1;
  }

  if(n === 1) {
    return 0;
  }

  return fib(n - 1) + fib(n - 2);
}

// Time Complexity: O(n)
// Space Complexity: O(n)
const fibI = (n, memoize = { 1: 0, 2: 1 }) => {
  if(n in memoize) {
    return memoize[n]
  }

  memoize[n] = fibI(n - 1) + fibI(n - 2);

  return memoize[n];
}

// Time Complexity: O(n)
// Space Complexity: O(1)
const fibII = (n) => {
  let first = 0;
  let second = 1;

  for(let i = 1; i < n; i++) {
    const temp = first;
    first = second;
    second = temp + second;
  }

  return first;
}

console.log(fibII(5));
