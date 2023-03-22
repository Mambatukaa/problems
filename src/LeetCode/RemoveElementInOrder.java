package LeetCode;

public class RemoveElementInOrder {
    private int[] nums;
    private int val;

    public RemoveElementInOrder(int[] nums, int val) {
        this.nums = nums;
        this.val = val;
    }

    public void swap(int[] nums, int leftIndex, int rightIndex) {
        int temp = nums[leftIndex];
        nums[leftIndex] = nums[rightIndex];
        nums[rightIndex] = temp;
    }


    // Time complexity: O(n)
    // Space complexity: O(1)
    public int naive() {
        int n = nums.length;
        int leftIndex = 0;
        int rightIndex = n - 1;

        while (leftIndex <= rightIndex) {
            int leftNum = nums[leftIndex];
            int rightNum = nums[rightIndex];

            if (leftNum != val && rightNum != val) {
                leftIndex++;
            }
            if (leftNum != val && rightNum == val) {
                leftIndex++;
                rightIndex--;
            }
            if (leftNum == val && rightNum != val) {
                swap(nums, leftIndex++, rightIndex--);
            }

            if (leftNum == val && rightNum == val) {
                rightIndex--;
            }

        }

        return rightIndex + 1;
    }

    // Time complexity: O(n)
    // Space complexity: O(1)

    public int solution() {
        int writer = 0;
        int reader = 0;
        int n = nums.length;

        while (reader < n) {
            if (nums[reader] == val) {
                reader++;
                continue;
            }
            nums[writer++] = nums[reader++];

        }

        return writer;
    }

}
