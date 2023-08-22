// Definition for singly-linked list.
 class ListNode {
     val: number
     next: ListNode | null
     constructor(val?: number, next?: ListNode | null) {
         this.val = (val===undefined ? 0 : val)
         this.next = (next===undefined ? null : next)
     }
}

// Time Complexity: O(n)
// Space Complexity: O(n)
function swapPairs(head: ListNode | null): ListNode | null {
  if(!head || !head.next) {
    return head;
  }


  const firstNode = head;
  const secondNode = head.next;


  // swapping
   firstNode.next = swapPairs(secondNode.next);
   secondNode.next = firstNode;

  return secondNode;

};

// Time Complexity: O(n)
// Space Complexity: O(1)
function swapPairsIteration(head: ListNode | null): ListNode | null {
  const dummy = new ListNode(-1, head);
  let prevNode = dummy;

  while(head && head.next) {
    const firstNode = head
    const secondNode = head.next;

    // swapping
    prevNode.next = secondNode;
    firstNode.next = secondNode.next;
    secondNode.next = firstNode;

    // update
    prevNode = firstNode;
    head = firstNode.next;
  }
  return dummy.next;
}

const head = new ListNode(1);
const node2 = new ListNode(2);
const node3 = new ListNode(3);
const node4 = new ListNode(4);

head.next = node2; 
node2.next = node3;
node3.next = node4;

traversal(head);
console.log('-------------------')
traversal(swapPairsIteration(head));


function traversal(head: ListNode | null) {
  while(head && head.val) {
    console.log(head.val, '-->');

    head = head.next;
  }

}
