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
var middleNode = function(head) {
    let slow = head;
    let fast = head;

    while(fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    };

    return slow;
};


/*
                            M
example 1: head = 1 -> 2 -> 3 -> 4 -> 5
output = 3 -> 4 -> 5

                                 M
example 2: head = 1 -> 2 -> 3 -> 4 -> 5 -> 6
output: 4 -> 5 -> 6


                       M
example 3: head = 1 -> 2
output: 2

number range [1,100]

1)
1. Iterate through linked list and find the linked lists's length
2. Divite length by 2. Ex1 length = 5, middleIndex = 5 / 2 => 2;
3. iterate i = 0 to middleIdx
4. update the dummyNode
5. return dummyNode.

Time Complexity: O(n / 2 + n) => O(n)
Space Complexity: O(1)


2) slow and fast pointers

                                      f               
                            s
example 1: head = 1 -> 2 -> 3 -> 4 -> 5 -> null

                                               f
                                 s
example 2: head = 1 -> 2 -> 3 -> 4 -> 5 -> 6

Time Complexity: O(n)
Space Complexity: O(1)

*/
