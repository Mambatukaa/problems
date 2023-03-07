package LeetCode;

public class FindEvenNumbersDigit {
    final private int[] nums;


    public FindEvenNumbersDigit(int[] nums) {
        this.nums = nums;
    }

    // Time complexity: O(n)
    // Space complexity: O(1)
    public int naive() {
        int counter = 0;

        for (int num : nums) {
            int numLength = Integer.toString(num).length();

            if (numLength % 2 == 0) {
                counter++;
            }

        }

        return counter;
    }


}
