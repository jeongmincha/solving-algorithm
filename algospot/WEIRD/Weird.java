import java.util.ArrayList;
import java.util.Scanner;

public class Weird {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numCase = sc.nextInt();
        for (int i = 0; i < numCase; i++) {
            int num = sc.nextInt();
            isWeird(num);
        }
    }

    private static ArrayList<Integer> properDivisors(int num) {
        ArrayList<Integer> divisors = new ArrayList<>();
        for (int n = 1; n < Math.sqrt(num); n++) {
            if (num % n == 0) {
                divisors.add(n);
                divisors.add(num / n);
            }
        }
        divisors.remove(new Integer(num));
        return divisors;
    }

    private static int sum(ArrayList<Integer> arr) {
        int sum = 0;
        for (int i = 0; i < arr.size(); i++) {
            sum += arr.get(i);
        }
        return sum;
    }

    private static boolean findSubset(ArrayList<Integer> arr,
        ArrayList<Integer> subset,
        int sum, int idx, int subsetIdx) {
        if (idx == arr.size()) {
            return false;
        }
        if (arr.get(idx) == sum) {
            subset.set(subsetIdx, arr.get(idx));
            return true;
        }
        for (int i = idx; i < arr.size(); i++) {
            if (arr.get(i) > sum) {
                continue;
            }
            if (arr.get(i) == sum) {
                subset.set(subsetIdx, arr.get(i));
                return true;
            }
            subset.set(subsetIdx, arr.get(i));
            if (findSubset(arr, subset, sum-arr.get(i), idx+1, subsetIdx+1)) {
                return true;
            }
        }
        return false;
    }

    private static boolean findSubsetSum(ArrayList<Integer> arr, int sum) {
        ArrayList<Integer> subset = new ArrayList<>();
        for (int i = 0; i < arr.size(); i++) {
            subset.add(0);
        }
        System.out.println(arr);
        System.out.println(subset);
        return findSubset(arr, subset, sum, 0, 0);
    }

    public static void isWeird(int num) {
        ArrayList<Integer> divisors = properDivisors(num);
        if (sum(divisors) < num) {
            return;
        }

        if (findSubsetSum(divisors, num)) {
            System.out.println("not weird");
        } else {
            System.out.println("weird");
        }
    }
}