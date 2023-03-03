import java.util.Scanner;

public class Test1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter size of array: ");
        int size = sc.nextInt();

        int [] array = new int[size];

        System.out.print("Enter elements of array: ");

        for(int i = 0; i < array.length; i++) {
           array[i] = sc.nextInt();
        }

        System.out.println(isMiddleLess(array));

    }

    public static int isMiddleLess(int [] array) {
        if(array.length % 2 == 0) {
            return 0;
        }

        if(array.length == 1) {
            return 1;
        }

        int middleNum = array[array.length / 2];

        System.out.println(middleNum + " middle num");

        for(int el: array) {
            if(el < middleNum) {
               return 0;
            }
        }

        return 1;
    };
}
