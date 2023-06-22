package LeetCode.LinkedList.Problems;

public class MergeTwoSortedLists {

    // Time complexity: O(n)
    // Space complexity: O(1)
    // use 3 pointers

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

        if (list1 == null) {
            return list2;
        }

        if (list2 == null) {
            return list1;
        }


        // update lists
        if (list1.val > list2.val) {
            ListNode temp = list1;
            list1 = list2;
            list2 = temp;
        }


        ListNode slow = list1;

        ListNode p1 = list1.next;
        ListNode p2 = list2;

        while (p2 != null) {
            traversal(list1);

            if (slow.next == null) {
                slow.next = p2;
                break;
            }

            System.out.println("p1: " + p1.val + " p2: " + p2.val);


            if (p1.val <= p2.val) {
                slow = p1;
                p1 = p1.next;
            } else {

                ListNode next = p2.next;
                p2.next = p1;
                slow.next = p2;
                slow = p2;
                p2 = next;
            }


        }


        return list1;

    }


    public void traversal(ListNode head) {
        ListNode temp = head;

        while (temp != null) {
            System.out.print(temp.val + " => ");

            temp = temp.next;
        }

        System.out.println();
    }
}
