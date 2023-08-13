package LeetCode.LinkedList.Problems;

public class RemoveNthNodeFromEnd {
    // naive solution
    // Time complexity: O(2N)
    // Space complexity: O(N)
    public ListNode naive(ListNode head, int n) {
        // 1. Find linked list's length
        int length = 0;
        ListNode temp = head;

        while (temp != null) {
            length++;
            temp = temp.next;
        }

        // edge case if length == n
        if (length == n) {
            return head.next;
        }

        // 2. Find index to remove
        int nodesBeforeRemovedIndex = length - n - 1;

        // 3. delete node that located in index
        temp = head;

        for (int i = 0; i < nodesBeforeRemovedIndex; i++) {
            temp = temp.next;
        }

        temp.next = temp.next.next;

        return head;
    }


    // two pointers
    // Time complexity: O(n)
    // Space complexity: O(1)

    public ListNode solution(ListNode head, int n) {
        ListNode currentNode = head;

        // move fast pointer n steps
        for (int i = 0; i < n; i++) {
            currentNode = currentNode.next;
        }

        // edge case
        if (currentNode == null) {
            return head.next;
        }

        // move two pointers
        ListNode nodeBeforeRemoved = head;

        while (currentNode.next != null) {
            currentNode = currentNode.next;
            nodeBeforeRemoved = nodeBeforeRemoved.next;
        }

        // remove node
        nodeBeforeRemoved.next = nodeBeforeRemoved.next.next;

        return head;
    }

}
