package LeetCode.LinkedList.Problems;

public class MergeTwoSortedLists {

    // Time complexity: O(n + m)
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


    // video solution
    // Time complexity: O(n + m)
    // Space complexity: O(1)
    public ListNode mergeTwoLists1(ListNode list1, ListNode list2) {
        ListNode head = new ListNode(0);
        ListNode tail = head;

        while (list1 != null && list2 != null) {

            if (list1.val < list2.val) {
                tail.next = list1;
                list1 = list1.next;
            } else {
                tail.next = list2;
                list2 = list2.next;
            }

            tail = tail.next;
        }

        tail.next = list1 == null ? list2 : list1;


        return head.next;
    }

    // video solution
    // recursive
    // Time complexity: O(n+m);
    // Space compleixty: O(n+m);

    public ListNode mergeTwoLists2(ListNode list1, ListNode list2) {
        // base case
        if (list1 == null) {
            return list2;
        }
        ;
        if (list2 == null) {
            return list1;
        }
        ;

        ListNode head;

        if (list1.val < list2.val) {
            head = list1;
            list1 = list1.next;
        } else {
            head = list2;
            list2 = list2.next;
        }

        head.next = mergeTwoLists(list1, list2);

        return head;
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
