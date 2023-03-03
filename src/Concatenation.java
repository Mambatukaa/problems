import java.util.Arrays;

public class Concatenation {
    public static int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n * 2];
        int j = 0;

        for (int i = 0; i < ans.length; i++) {
            ans[i] = nums[j];

            j++;

            if(j == n) {
                j = 0;
            }
        }

        return ans;
    }

    public static void main(String[] args) {
        int[] arr = new int[]{1, 2, 3, 4, 5};

        int[] response = getConcatenation(arr);

        System.out.println(Arrays.toString(response));
    }
}
