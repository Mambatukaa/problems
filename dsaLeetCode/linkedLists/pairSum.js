/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {number}
 */
// Time Complexity: O(n)
// Space Complexity: O(n)
var pairSumII = function(head) {
  let max = -Infinity;
  const arr = [];

  while(head) {
    arr.push(head.val);
    head = head.next;
  };

  let leftIdx = 0;
  let rightIdx = arr.length - 1;

  while(leftIdx < rightIdx) {
    const sum = arr[leftIdx] + arr[rightIdx];

    if(sum > max) {
      max = sum;
    };

    leftIdx++;
    rightIdx--;
  };
    
  return max;
};

// Time Complexity: O(n)
// Space Complexity: O(1)
var pairSum = function(head) {
  let slow = head;
  let fast = head;

  while(fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  };

  let reversedHead = null;

  while(slow) {
    const next = slow.next;

    slow.next = reversedHead;
    reversedHead = slow;

    slow = next;
  };

  let max = -Infinity;

  while(reversedHead) {
    const sum = reversedHead.val + head.val;

    if(sum > max) {
      max = sum;
    }

    head = head.next;
    reversedHead = reversedHead.next;
  };


return max;


};


/*
       1    2    2    1
head = 5 -> 4 -> 2 -> 1;
output: 6

pairs(1,1) = 5 + 1 = 6;
pairs(2,2) = 4 + 2 = 6;
max = 6;

1. use arr = [];
2. elements to the arr = [5,4,2,1];
3. use two pointers and update the answer L=0; R=arr[length] - 1;
4. while(L < R) {
   if(max < arr[l] + arr[r]) {
     max = arr[l] + arr[i];
   }
   l++;
   r--;
}
   Time Complexity: O(n)
   Space Complexity: O(n)


------------------------------------------------------------------------------------------------------------------------------------------------
       1    2    3    3    2    1
head = 1 -> 2 -> 3 -> 4 -> 5 -> 6
output: 7

pairs(1,1) = 1 + 6 = 7;
pairs(2,2) = 2 + 5 = 7;
pairs(3,3) = 3 + 4 = 7;
max = 7;

Linked lists length is even
1 <= nodeValue < 10^5





Reverse

                    s
                             f
   head = 1 -> 2 -> 3 -> 4
reverse = 

p  s
   3 -> 4
   p
<- 3 <- s 

prev = null

nextNode = s.next;
s.next = prev;
prev = s;
s = nextNode;


reversedHead = 4 -> 3;
        head = 1 -> 2;

let max = -Infinity;
while(head) {
  if(reversedHead.val + head.val > max) {
    max = reversedHead.val + head.val;
  };
  
  head = head.next;
  reversedHead = reversedHead.next;
};

return max;

length / 2
sum = reversedHead + head;

reversedHead = reversedHead.next;
head = head.next;

*/
