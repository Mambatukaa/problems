package AlgoExpert.array;

import java.util.Hashtable;

public class TwoNumberSum1 {
    final private int[] array;
    final private int target;


    public TwoNumberSum1(int[] array, int target) {
        this.array = array;
        this.target = target;
    }

    public int[] solution() {
        Hashtable<Integer, Integer> hashtable = new Hashtable<>();

        for (int i = 0; i < array.length; i++) {
            int diff = target - array[i];

            if (hashtable.containsKey(diff)) {
                int diffIndex = hashtable.get(diff);

                return new int[]{diffIndex, i};
            }

            hashtable.put(array[i], i);

        }

        System.out.println(hashtable);

        return null;
    }


}
