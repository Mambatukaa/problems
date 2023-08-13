package LeetCode.LinkedList.Problems;

import java.util.HashSet;

public class LinkedListCycle {


    public boolean hasCycleSet(ListNode head) {
        // hashMap solution
        // Time complexity: O(n)
        // Space complexity: O(n)

        HashSet<ListNode> nodesSeen = new HashSet<>();

        while (head != null) {
            if (nodesSeen.contains(head)) {
                return true;
            }

            nodesSeen.add(head);

            head = head.next;
        }

        return false;
    }

    public boolean hasCyclePointers(ListNode head) {
        // two pointer solution
        // Time complexity: O(n)
        // Space complexity: O(1)

        if (head == null) {
            return false;
        }

        ListNode slow = head;
        ListNode fast = head.next;

        while (slow != fast) {
            if (fast == null || fast.next == null) {
                return false;
            }

            slow = slow.next;
            fast = fast.next.next;
        }

        return true;
    }
}
