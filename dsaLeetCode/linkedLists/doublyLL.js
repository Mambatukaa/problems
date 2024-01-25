class ListNode {
  constructor(value) {
    this.value = value;
    this.next = null;
    this.prev = null;
  };
};

const returnMidElement = (head) => {
  let slow = head;
  let fast = head;

  while(fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  };

  return slow.value;
};


const head = new ListNode(1);

const node2 = new ListNode(2)
const node3 = new ListNode(3)
const node4 = new ListNode(4)

const tail = new ListNode(5)

head.next = node2;

node2.prev = head;
node2.next = node3;

node3.prev = node2;
node3.next = node4;

node4.prev = node3;
node4.next = tail;
tail.prev = node4;


console.log(returnMidElement(head));


