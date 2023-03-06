package LeetCode;

import java.util.Collection;
import java.util.Hashtable;

public class NumberOfGoodPairs {
    final private int[] nums;


    public NumberOfGoodPairs(int[] nums) {
        this.nums = nums;
    }

    // Space complexity: O(1)
    // Time complexity: O(n^2)
    public int naive() {
        int count = 0;
        int length = nums.length;

        for (int i = 0; i < length; i++) {
            int current = nums[i];

            for (int j = i + 1; j < length; j++) {
                if (current == nums[j]) {
                    count++;
                }

            }
        }

        return count;
    }


    public int solution() {
//        Hashtable<Integer, Integer> hashtable = new Hashtable<>();
//
//        for (int num : nums) {
//            if (hashtable.containsKey(num)) {
//                int count = hashtable.get(num);
//                hashtable.replace(num, ++count);
//            } else {
//                hashtable.put(num, 0);
//            }
//        }
//
//        System.out.println(hashtable);
//
//        int counter = 0;
//
//        Collection<Integer> values = hashtable.values();
//
//        for (int value : values) {
//            counter += value;
//        }
//        System.out.println("hahah");
//
//        return counter;

        return 1;
    }

}
