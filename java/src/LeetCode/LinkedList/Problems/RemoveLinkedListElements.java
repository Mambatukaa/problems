package LeetCode.LinkedList.Problems;

public class RemoveLinkedListElements {
    // input: [1,2,6,3,4,5,6] val = 6;
    // remove all elements which equal val

    // Time complexity: O(n)
    // Space complexity: O(1)
    // 2 pointers solution
    public ListNode solution(ListNode head, int val) {

        // edge case
        if (head == null) {
            return head;
        }

        ListNode current = head;
        ListNode dummy = null;
        ListNode prev = new ListNode(0);

        while (current != null) {
            if (current.val != val) {
                if (dummy == null) {
                    dummy = current;
                }

                prev = current;
            } else {
                prev.next = current.next;
            }

            current = current.next;
        }


        return dummy;
    }
}
