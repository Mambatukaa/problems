package LeetCode.LinkedList;

public class CircularSinglyLinkedList {
    public Node head;
    public Node tail;
    public int size;

    // Time complexity: O(1)
    // Space complexity: O(1)
    public Node createCSLL(int nodeValue) {
        head = new Node();
        Node node = new Node();
        node.value = nodeValue;
        node.next = node;
        head = node;
        tail = node;
        size = 1;

        return head;
    }


    // Time complexity: O(n)
    // Space complexity: O(1)
    public void insert(int location, int nodeValue) {
        // if CSLL doesn't exist
        if (size == 0) {
            createCSLL(nodeValue);
            return;
        }

        Node node = new Node();
        node.value = nodeValue;

        // beginning
        if (location == 0) {
            node.next = head;
            head = node;

            // update tail next
            tail.next = head;
        }
        // end
        else if (location >= size) {
            tail.next = node;
            tail = node;
            node.next = head;
        }
        // mid
        else {
            Node temp = head;

            for (int i = 0; i < location - 1; i++) {
                temp = temp.next;
            }

            node.next = temp.next;
            temp.next = node;
        }

        size++;
    }


    // Time complexity: O(n)
    // Space complexity: O(1)
    public void traversal() {
        if (size == 0) {
            System.out.println("CSLL doesn't exist.");
            return;
        }

        Node temp = head;

        for (int i = 0; i < size; i++) {
            System.out.print(temp.value);

            if (i != size - 1) {
                System.out.print(" --> ");
            }

            temp = temp.next;
        }
        System.out.println();
    }

    public boolean search(int nodeValue) {
        if (size == 0) {
            System.out.println("CSLL doesn't exist.");
            return false;
        }

        Node temp = head;

        for (int i = 0; i < size; i++) {
            if (temp.value == nodeValue) {
                System.out.println("Found at " + i);
                return true;
            }

            temp = temp.next;
        }

        System.out.println("Not found!");

        return false;
    }


    // Space complexity: O(1)
    // Time complexity: O(n)
    public void delete(int location) {
        if (head == null) {
            System.out.println("CSLL doesn't exist!");
            return;
        }

        // beginning
        if (location == 0) {
            // tail ==> second node
            // head ==> new node
            head = head.next;
            tail.next = head;
            size--;

            if (size == 0) {
                head.next = null;
                head = null;
                tail = null;
            }
        }
        // end
        else if (location >= size) {
            // beforeTail.next ==> head
            // tail = beforeTail;
            Node tempNode = head;

            for (int i = 0; i < size - 1; i++) {
                tempNode = tempNode.next;
            }

            tempNode.next = head;
            tail = tempNode;
            size--;

            if (size == 0) {
                head.next = null;
                head = null;
                tail = null;
            }
        }
        // middle
        else {
            // find element before location
            // beforeElement ==> beforeElement.next.next
            Node temp = head;

            for (int i = 0; i < location - 1; i++) {
                temp = temp.next;
            }

            temp.next = temp.next.next;
            size--;
        }


    }

    // Time complexity: O(1)
    // Space complexity: O(1)
    public void deleteEntireCSLL() {
        if (head == null) {
            System.out.println("CSLL doesn't exist");
            return;
        }
        head = null;
        tail.next = null;
        tail = null;
        size = 0;

        System.out.println("Successfully deleted a CSLL.");
    }


}
