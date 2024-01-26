class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }


};

// Time Complexity: O(n)
// Space Complexity: O(1)
var reverseList = function(head) {
    let prev = null
    
    while(head) {
       let dummy = head.next;
        head.next = prev;
    
        prev = head;
        head = dummy;
    }

    return prev;
};


// Time Complexity: O(n)
// Space Complexity: O(n)
const recursive = (head, prev = null) => {
  if(!head) {
    return prev;
  }

  const next = head.next;
  head.next = prev;

  return fn(next, head);
}

const head = new ListNode(1);

const node2 = new ListNode(2);
const node3 = new ListNode(3);

const node4 = new ListNode(4);
const node5 = new ListNode(5);

head.next = node2;
node2.next = node3;
node3.next = node4;
node4.next = node5;

console.log(recursive(head));
