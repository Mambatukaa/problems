package LeetCode.LinkedList.Problems;

public class OddEvenLinkedList {

    // Time complexity: O(n)
    // Space complexity: O(1)
    // Connecting odd to even
    public ListNode solution(ListNode head) {
        if (head == null) return head;

        ListNode odd = head;
        ListNode even = head.next;
        ListNode evenHead = even;

        while (even != null && even.next != null) {
            odd.next = even.next;
            odd = odd.next;

            even.next = odd.next;
            even = even.next;
        }


        // connecting odd to the even
        odd.next = evenHead;

        return head;
    }
}
