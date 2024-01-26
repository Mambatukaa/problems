class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  };
};

// Time Complexity: O(n)
// Space Complexity: O(1)
const fn = (head, k) => {
  let slow = head;
  let fast = head;

  for(let i = 0; i < k; i++) {
    fast = fast.next;
  }

  while(fast) {
    slow = slow.next;
    fast = fast.next;
  };

  return slow;

};

const head = new ListNode(1);

const node2 = new ListNode(2);
const node3 = new ListNode(3);

const node4 = new ListNode(4);
const node5 = new ListNode(5);

head.next = node2;
node2.next = node3;
node3.next = node4;
node4.next = node5;

console.log(fn(head, 4));

// Kth node from the end
