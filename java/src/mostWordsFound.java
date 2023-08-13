import java.util.Arrays;

class MostWordsFound {

//    static final int OUT = 0;
//    static final int IN = 1;
//
//    static int countWords(String str)
//    {
//        int state = OUT;
//        int wc = 0;  // word count
//        int i = 0;
//
//        // Scan all characters one by one
//        while (i < str.length())
//        {
//            // If next character is a separator, set the
//            // state as OUT
//            if (str.charAt(i) == ' ' || str.charAt(i) == '\n'
//                    || str.charAt(i) == '\t')
//                state = OUT;
//
//                // If next character is not a word separator
//                // and state is OUT, then set the state as IN
//                // and increment word count
//            else if (state == OUT)
//            {
//                state = IN;
//                ++wc;
//            }
//
//            // Move to next character
//            ++i;
//        }
//        return wc;
//    }

    public static int mostWordsFound(String[] sentences) {
        int max = Integer.MIN_VALUE;

        for (String sentence : sentences) {
            int count = 1;

            for(int i = 0; i < sentence.length(); i++) {
                if(sentence.charAt(i) == ' ') {
                    count++;
                }
            }

            if(count > max) {
                max = count;
            }

        }

        return max;
    };

    public static void main(String[] args) {
        String[] sentences = new String[]{"a", "1 2 3"};

        int response = mostWordsFound(sentences);
        System.out.println(response);

    }
}
