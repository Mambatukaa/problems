 /* Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycleII = function(head) {
    let slow = head;
    let fast = head;

    while(fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;

        if(slow === fast) {
            return true;
        }
    }
    
    return false;
};

var hasCycle = function(head) {
    let dummy = head;
    const set = new Set();

    while(dummy) {
        if(set.has(dummy)) return true;
        set.add(dummy);

        dummy = dummy.next;
    }
    
    return false;
}

/*

       f.        f.         f. 
       s.   s.   s.    s.   s.   s 
head = 3 => 2 => 0 => -4 => 3 => 2 => .....


1. Use set. TC: O(n) SC: O(n)
2. fast and slow TC: O(n) SC: O(1)

Core Strategy
For this problem, let's see what will happen if there's a circle.
If it's a little abstract, then let's think about we are running on a circular track.

If the track is 100m long, your speed is 10m/s, your friend's speed is 5m/s. Then after 20s, you've run 200m, your friend has run 100m. But because the track is circular, so you will be at the same place with your friend since the difference between your distances is exactly 100m.

How about we change another track, change the speed of you and your friend? As long as your speeds are not the same, the faster person will always catch up with the slower person again.

That's the key point for this problem.



*/
