public class Test6 {

    static int point(int[] nums) {
        if(nums.length < 3) return -1;
        // POE point of equilibrium
        int i = 0;
        int j = nums.length - 1;

        int idx = 1;
        int leftSum = nums[i];
        int rigthSum = nums[j];

        for(int k = 0; k < nums.length - 2; k++) {
            if(leftSum < rigthSum) {
                i++;
                leftSum += nums[i];
                idx = i + 1;
            } else {
                j--;
                rigthSum += nums[j];

                idx = j - 1;
            }

            if(leftSum == rigthSum) {
                return idx;
            } else {
                return -1;
            }
        }

        return 1;
    }

    public static void main(String[] args) {
        int[] nums = new int[]{1, 2, 0, 1};

        int response = point(nums);

        System.out.println(response);
    }
}
