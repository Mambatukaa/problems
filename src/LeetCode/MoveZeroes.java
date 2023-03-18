package LeetCode;

public class MoveZeroes {
    final private int[] nums;

    public MoveZeroes(int[] nums) {
        this.nums = nums;
    }

    public void swap(int[] nums, int leftIndex, int rightIndex) {
        int tmp = nums[leftIndex];
        nums[leftIndex] = nums[rightIndex];
        nums[rightIndex] = tmp;
    }

    public int[] naive() {
        int leftIndex = 0;
        int rightIndex = 1;
        int n = nums.length;

        while (rightIndex < n) {
            int leftNum = nums[leftIndex];
            int rightNum = nums[rightIndex];

            if (leftNum != 0) {
                leftIndex++;
                rightIndex++;
            } else if (rightNum == 0) {
                rightIndex++;
            } else {
                swap(nums, leftIndex++, rightIndex++);
            }

        }


        return nums;
    }


}
