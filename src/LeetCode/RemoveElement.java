package LeetCode;

public class RemoveElement {
    final private int[] nums;
    final private int val;

    public RemoveElement(int[] nums, int val) {
        this.nums = nums;
        this.val = val;
    }

    public void swap(int[] nums, int index1, int index2) {
        int temp = nums[index1];
        nums[index1] = nums[index2];
        nums[index2] = temp;
    }

    // Time complexity: O(n)
    // Space complexity: O(1)
    public int naive() {
        int i = 0;

        for (int j = 0; j < nums.length; j++) {
            if (nums[j] != val) {
                nums[i] = nums[j];
                i++;
            }
        }

        return i;
    }

    // Time complexity: O(n)
    // Space complexity: O(1)
    // When remove element is rare
    public int solution() {
        int p1 = 0;
        int p2 = nums.length - 1;

        while (p1 <= p2) {
            if (nums[p1] == val) {
                nums[p1] = nums[p2];
                p2--;
            } else {
                p1++;
            }
        }

        return p1;
    }

}
