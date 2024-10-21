import java.util.Scanner;

public class Palindrome {
    public static boolean isPalindrome(String a) {
        int n = a.length();
        for (int i = 0; i < n / 2; i++) {
            if (a.charAt(i) != a.charAt(n - 1 - i)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner vis = new Scanner(System.in);
        System.out.println("Enter a string to check:");
        String a = vis.nextLine();
        if (isPalindrome(a)) {
            System.out.println("The given string is a palindrome.");
        } else {
            System.out.println("The given string is not a palindrome.");
        }
        vis.close();
    }
}
