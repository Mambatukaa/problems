import java.util.Arrays;

public class DuplicatesZero {


    static void insertElement(int[] nums, int idx) {
        for(int i = nums.length - 2; i >= idx; i--) {
            System.out.println(nums[i+1] + " ----- " + nums[i]);
            nums[i + 1] = nums[i];
        }
        System.out.println("--------------------");
    }

    static void point(int[] nums) {
        // if nums[i] == 0 ? shift element to right
        // update nums[i + 1] = 0

        for(int i = nums.length - 2; i >= 0; i--) {
            if(nums[i] == 0) {
                insertElement(nums, i);
            }
        }
    }

    public static void main(String[] args) {
        int[] nums = new int[]{1, 0, 2, 3, 0, 4, 5, 0}; // 0,0,5,0,0
//        int[] nums = new int[]{0, 0, 1, 0}; // 0,0,5,0,0

        point(nums);

        System.out.println(Arrays.toString(nums));
    }
}
