import LeetCode.*;

class Main {
    public static void main(String[] args) {
        int[] nums = {0, 0, 0, 0, 1, 1};

        MaxConsecutiveOnesII maxConsecutiveOnesII = new MaxConsecutiveOnesII(nums);

        System.out.println(maxConsecutiveOnesII.naiveLC());
    }

}
