import { ListNode } from './swapNodesInPairs';


const node5 = new ListNode(5);
const node4 = new ListNode(4, node5);
const node3 = new ListNode(3, node4);
const node2 = new ListNode(2, node3);

const head = new ListNode(1, node2);


// Time Complexity: O(n)
// Space Complexity: O(1)
const reverse = (head: ListNode | null) => {
  let prev: ListNode | null = null;
  let curr = head;

  while(curr) {
    const nextTemp = curr.next;
    curr.next = prev;

    prev = curr;
    curr = nextTemp;
  }

  return prev;
}

// Time Complexity: O(n)
// Space Complexity: O(n)
const reverseRecursion = (head: ListNode | null): any => {
  if(!head || !head.next) {
    return head;
  }

  const newHead = reverseRecursion(head.next);

  head.next.next = head;
  head.next = null;

  return newHead;
}

let reversed = reverseRecursion(head);

while(reversed) {
  console.log(reversed.val);

  // @ts-ignore
  reversed = reversed.next;
}


