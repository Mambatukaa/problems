import java.util.Scanner;

public class ReverseInt {
    public static void main(String[] args) {
        ReverseInt obj = new ReverseInt();
        Scanner sc = new Scanner(System.in);

        System.out.println("Please enter a number: ");

        int num = sc.nextInt();

        int response = obj.reverseNumber(num);

        System.out.println(response);
    }

    int reverseNumber(int num) {
        // is num positive or negative
        int sign = 1;

        // if num === 0 will return 0
        if (num == 0) return 0;

        // if num is negative change to num to positive and change sign
        if (num < 0) {
            sign = -1;
            num = -num;
        }


        int reverse = 0;

        // num still more than one loop will work
        while (num >= 1) {
            reverse = (reverse * 10) + (num % 10);
            num /= 10;
        }


        return reverse * sign;
    }

}
