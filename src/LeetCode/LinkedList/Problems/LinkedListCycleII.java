package LeetCode.LinkedList.Problems;

import java.util.HashSet;

public class LinkedListCycleII {

    // hash set solution
    // Time complexity: O(n)
    // Space complexity: O(n)
    public ListNode naive(ListNode head) {

        HashSet<ListNode> nodesSeen = new HashSet<>();

        while (head != null) {
            if (nodesSeen.contains(head)) {
                return head;
            }

            nodesSeen.add(head);

            head = head.next;
        }

        return null;
    }


    public ListNode getIntersect(ListNode head) {
        ListNode tortoise = head;
        ListNode hare = head;

        while (hare != null && hare.next != null) {
            tortoise = tortoise.next;
            hare = hare.next.next;

            if (hare == tortoise) {
                return tortoise;
            }
        }

        return null;

    }

    // fast and slow solution
    // Time complexity: O(n)
    //
    public ListNode solution(ListNode head) {
        if (head == null) {
            return null;
        }


        ListNode intersect = getIntersect(head);

        if (intersect == null) {
            return null;
        }

        ListNode ptr1 = head;
        ListNode ptr2 = intersect;


        while (ptr1 != ptr2) {
            ptr1 = ptr1.next;
            ptr2 = ptr2.next;
        }

        return ptr1;
    }


}
