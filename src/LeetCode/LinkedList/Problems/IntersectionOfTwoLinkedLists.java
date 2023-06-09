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
}
