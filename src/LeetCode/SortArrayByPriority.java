package LeetCode;

public class SortArrayByPriority {
    final private int[] nums;

    public SortArrayByPriority(int[] nums) {
        this.nums = nums;
    }

    public void swap(int[] nums, int leftIndex, int rightIndex) {
        int temp = nums[leftIndex];
        nums[leftIndex] = nums[rightIndex];
        nums[rightIndex] = temp;
    }

    // Time complexity: O(n)
    // Space complexity: O(1)
    public int[] naive() {

        int leftIndex = 0;
        int rightIndex = 1;
        int n = nums.length;


        while (rightIndex < n) {
            int leftNum = nums[leftIndex];
            int rightNum = nums[rightIndex];
            boolean isLeftEven = leftNum % 2 == 0;
            boolean isRightEven = rightNum % 2 == 0;

            if (isLeftEven) {
                leftIndex++;
            } else if (isRightEven) {
                swap(nums, leftIndex, rightIndex);
                leftIndex++;
            }

            rightIndex++;

        }

        return nums;
    }


}
