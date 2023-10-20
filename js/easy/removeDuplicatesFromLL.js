// Sorted linked list
// Time Complexity: O(n)
// Space Complexity: O(1)
const removeDuplicates = (head) => {
  let left = head;
  let right = head.next;

  while(right) {
    if(left.value !== right.value) {
      left.next = right;
      left = right;
    }

    right = right.next;
  }

  left.next = right;

  return head;
};

// Sorted linked list
// Time Complexity: O(n)
// Space Complexity: O(1)
const removeDuplicatesII = (head) => {
  let curr = head;

  while(curr.next) {
    if(curr.value === curr.next.value) {
      curr.next = curr.next.next;
    } else {
      curr = curr.next;
    }
  }

  console.log(head);

  return head;
}

// Sorted linked list
// Time Complexity: O(n)
// Space Complexity: O(1)
const removeDuplicatesIII = (head) => {
  let curr = head;

  while(curr) {
    let next = curr.next;

    while(next && curr.value === next.value) {
      next = next.next;
    }

    curr.next = next;
    curr = next;
  }

  return head;
}

// UnSorted linked list
// Time Complexity: O(n)
// Space Complexity: O(n)
const removeDuplicatesIV = (head) => {
  let curr = head;
  let set = new Set();

  set.add(curr.value);

  while(curr.next) {
    if(!set.has(curr.next.value)) {
      set.add(curr.next.value);
      curr = curr.next;
    } else {
      curr.next = curr.next.next;
    }
  }

  let temp = head;

  while(temp) {
    console.log(temp.value);

    temp = temp.next;
  }

  return head;
}

class LinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}


const head = new LinkedList(1);

const node2 = new LinkedList(1);
const node3 = new LinkedList(3);

const node4 = new LinkedList(4);
const node5 = new LinkedList(4);

const node6 = new LinkedList(4);
const node7 = new LinkedList(5);

const node8 = new LinkedList(6);
const node9 = new LinkedList(6);

head.next = node2;
node2.next = node3;
node3.next = node4;

node4.next = node5;
node5.next = node6;

node6.next = node7;
node7.next = node8;

node8.next = node9;

removeDuplicatesIV(head);
