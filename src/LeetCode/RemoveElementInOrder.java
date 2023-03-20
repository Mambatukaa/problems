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


    //
    //
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
}
