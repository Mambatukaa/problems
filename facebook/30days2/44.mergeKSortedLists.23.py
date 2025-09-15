""""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.











"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeTwoLists(p1, p2):
            head = ListNode(0)
            dummy = head

            while p1 and p2:
                if p1.val < p2.val:
                    dummy.next = p1
                    p1 = p1.next
                else:
                    dummy.next = p2
                    p2 = p2.next
                dummy = dummy.next

            while p1:
                dummy.next = p1
                dummy = dummy.next
                p1 = p1.next

            while p2:
                dummy.next = p2
                dummy = dummy.next
                p2 = p2.next

            return head.next

        n = len(lists)

        for i in range(n - 1):
            p1 = lists[i]
            p2 = lists[i + 1]

            merged_list = mergeTwoLists(p1, p2)


            lists[i + 1] = merged_list

        return lists[-1]


        
class HeapNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        # Define comparison based on ListNode's value
        return self.node.val < other.node.val


# Time Complexity: O(n logk)
# Space Complexity: O(n)
class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        heap = []

        # Initialize the heap
        for l in lists:
            if l:
                heapq.heappush(heap, HeapNode(l))

        # Extract the minimum node and add its next node to the heap
        while heap:
            heap_node = heapq.heappop(heap)
            node = heap_node.node
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, HeapNode(node.next))

        return dummy.next
