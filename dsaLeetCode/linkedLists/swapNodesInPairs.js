class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }

};

const swapNodesInPairs = (head) => {
  if(!head || !head.next) return head;

  const v1 = head, v2 = head.next, v3 = v2.next;

  v2.next = v1;
  v1.next = swapNodesInPairs(v3);

  return v2;
};


const head = new ListNode(1);

const node2 = new ListNode(2);
const node3 = new ListNode(3);
const node4  = new ListNode(4);
const node5  = new ListNode(5);
const node6  = new ListNode(6);

head.next = node2;
node2.next = node3;
node3.next = node4;
node4.next = node5;
node5.next = node6;

console.log(swapNodesInPairs(head))

