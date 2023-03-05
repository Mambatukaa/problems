package LeetCode;

public class LeftAndRightSumDifferences {
    private final int[] nums;


    public LeftAndRightSumDifferences(int[] nums) {
        this.nums = nums;
    }

    private int[] calculateLeftSum(int[] nums) {
        int[] leftSum = new int[nums.length];
        int sumTracker = 0;
        int currentIndex = 1;

        for (int i = 0; i < nums.length - 1; i++) {
            sumTracker += nums[i];
            leftSum[currentIndex] = sumTracker;
            currentIndex++;
        }

        return leftSum;
    }

    private int[] calculateRightSum(int[] nums) {
        int[] rightSum = new int[nums.length];
        int sumTracker = 0;
        int currentIndex = nums.length - 2;

        for (int i = nums.length - 1; i > 0; i--) {
            sumTracker += nums[i];
            rightSum[currentIndex] = sumTracker;
            currentIndex--;
        }

        return rightSum;
    }

    public int[] naive() {
        System.out.println("Starting...");

        int[] leftSum = this.calculateLeftSum(nums);
        int[] rightSum = this.calculateRightSum(nums);


        int[] ans = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            int left = leftSum[i];
            int right = rightSum[i];

            ans[i] = Math.abs(left - right);
        }

        return ans;
    }

}
