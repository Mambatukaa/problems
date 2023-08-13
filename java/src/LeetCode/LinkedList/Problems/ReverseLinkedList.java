package LeetCode.LinkedList.Problems;

public class ReverseLinkedList {
    // Time complexity: O(n)
    // Space complexity: O(1)
    // move head.next to the head solution
    public ListNode solution(ListNode head) {
        // edge case
        if (head == null) {
            return head;
        }

        ListNode currentHead = head;

        while (head.next != null) {
            ListNode p = head.next;
            head.next = p.next;
            p.next = currentHead;
            currentHead = p;
        }

        return currentHead;
    }

}
