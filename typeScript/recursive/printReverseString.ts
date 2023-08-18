const reverse = (index: number, str: string) => {
  if(!str || index >= str.length) {
    return;
  }

  reverse(index + 1, str);

  console.log(str[index]);
}


// using two pointers
// Time Complexity: O(n)
// Space Complexity: O(1)
const reverseString = (s: string[]): void => {
  let leftIndex = 0;
  let rightIndex = s.length - 1;

  while(leftIndex < rightIndex) {
    const temp = s[leftIndex];
    s[leftIndex] = s[rightIndex];
    s[rightIndex] = temp;

    leftIndex++;
    rightIndex--;
  }

}


// using two pointers
// Time Complexity: O(n)
// Space Complexity: O(n)
const reverseStringRecursive = (s: string[]): void => {
  let leftIndex = 0;
  let rightIndex = s.length - 1;

  const reverse = (s: string[], leftIndex: number, rightIndex: number) => {
    if(leftIndex >= rightIndex) {
      return;
    }

    const temp = s[leftIndex];
    s[leftIndex] = s[rightIndex];
    s[rightIndex] = temp;

    reverse(s, leftIndex + 1, rightIndex - 1);
  }


  reverse(s, leftIndex, rightIndex);

}

const s = ["h", "e", "l", "l", "o", "o"];

reverseStringRecursive(s);

console.log('updated string: ', s);
