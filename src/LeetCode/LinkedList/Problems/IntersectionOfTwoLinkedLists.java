package LeetCode.LinkedList.Problems;

import java.util.HashSet;

public class IntersectionOfTwoLinkedLists {
    // Time complexity: O(n+m)
    // Space complexity: O(n)
    public ListNode hashSetSolution(ListNode headA, ListNode headB) {
        HashSet<ListNode> visited = new HashSet<>();

        // loop through head A
        while (headA != null) {
            visited.add(headA);
            headA = headA.next;
        }

        // loop through head B
        while (headB != null) {
            if (visited.contains(headB)) {
                return headB;
            }

            headB = headB.next;
        }

        return null;
    }


    // Time complexity: O(N+M)
    // Space complexity: O(1)
    // Solution for two pointers
    public ListNode solution(ListNode headA, ListNode headB) {
        ListNode ptr1 = headA;
        ListNode ptr2 = headB;


        while (ptr1 != ptr2) {
            ptr1 = ptr1 == null ? headB : ptr1.next;
            ptr2 = ptr2 == null ? headA : ptr2.next;
        }

        return ptr1;
    }
}
