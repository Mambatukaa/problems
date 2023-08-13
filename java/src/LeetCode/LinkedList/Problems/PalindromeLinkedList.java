package LeetCode.LinkedList.Problems;

public class PalindromeLinkedList {
    // Solution
    // Time complexity: O(n)
    // Space complexity: O(1)
    // second half reverse solution


    public boolean isPalindrom(ListNode head) {
        // Find middle
        ListNode firstOfSecondHalf = findFirstOfSecondHalf(head);

        // Reverse second half
        ListNode reversedHead = reverseSecondHalf(firstOfSecondHalf);

        // Compare first half and second half
        while (reversedHead != null) {
            if (head.val != reversedHead.val) {
                return false;
            }

            head = head.next;
            reversedHead = reversedHead.next;
        }

        return true;
    }


    public ListNode findFirstOfSecondHalf(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        return slow.next;
    }

    public ListNode reverseSecondHalf(ListNode head) {
        ListNode prev = null;

        while (head != null) {
            ListNode temp = head.next;
            head.next = prev;
            prev = head;
            head = temp;
        }

        return prev;
    }
}
