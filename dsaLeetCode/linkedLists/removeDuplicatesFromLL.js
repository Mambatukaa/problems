/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */

// Time Complexity: O(n)
// Space Complexity: O(1)
var deleteDuplicates = function(head) {
    let p1 = head;
    let p2 = head;

    while(p2) {
        if(p1.val === p2.val) {
            // remove
            p1.next = p2.next;
        } else {
            p1 = p1.next;
        };
        
        p2 = p2.next;
    }
    
    return head;
};


/*

input: head = 1 -> 1 -> 2
output: head = 1 -> 2

The list is sorted in ascending order.

example: 1
                   R
input: head = 1 -> 1 -> 2

example 2:

1)

              c    R         c
                   R              R
input: head = 1 -> 1 -> 2 -> 3 -> 3 -> null
       remove c.next = c.next.next
       remove c.next = c.next.next
       
       while(curr.next)

       return head;

set = [1, 2, 3]

1. Find duplicates using additional DS set.
2. check value from set and add value to set. 
3. If value is in set. Remove the node.
4. After checking the every node.
5. Return head;

Time Complexity: O(n)
Space Complexity: O(n)

2) 

                  p1   
                        p2
input: head = 1 -> 3 -> null

if(p1 === p2) {
    // remove
    p1.next = p2.next;
    p2 = p2.next;
} else {
    p1 = p1.next;
    p2 = p2.next;
};

return head;

Time Complexity: O(n)
Space Complexity: O(1)


*/
