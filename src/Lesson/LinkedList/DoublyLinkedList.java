package Lesson.LinkedList;

public class DoublyLinkedList {
    public DoublyNode head;
    public DoublyNode tail;
    public int size;


    // Time complexity: O(1)
    // Space complexity: O(1)
    public DoublyNode create(int nodeValue) {
        head = new DoublyNode();
        DoublyNode node = new DoublyNode();
        node.value = nodeValue;
        node.next = null;
        node.previous = null;
        head = node;
        tail = node;

        size = 1;

        return head;
    }

    public void insert(int location, int nodeValue) {
        if (size == 0) {
            create(nodeValue);
            return;
        }

        DoublyNode newNode = new DoublyNode();
        newNode.value = nodeValue;

        // beginning
        // new head
        // head.next.prev will change
        if (location == 0) {
            if (size == 1) {
                newNode.next = head;
            } else {

            }

            head.next.previous = newNode;
            head = newNode;
            size++;
        }
        // end
        else if (location >= size) {
            // newNode.previous = tail;
            // tail.next = newNode;
            // tail = newNode;
            newNode.previous = tail;
            tail.next = newNode;
            tail = newNode;

            size++;
        }
        // middle
        else {
            // find insert position
            //
            DoublyNode temp = head;

            for (int i = 0; i < location - 1; i++) {
                temp = temp.next;
            }

            newNode.previous = temp;
            newNode.next = temp.next;
            temp.next.previous = newNode;
            temp.next = newNode;

            size++;
        }

        System.out.println("Successfully inserted...");

    }
}
