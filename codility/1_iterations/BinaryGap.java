import java.util.ArrayList;

class Solution {
    public int solution(int N) {
        int n = N;
        ArrayList<Integer> binaryList = new ArrayList<Integer>();

        while (n > 0) {
            binaryList.add(n % 2);
            n /= 2;
        }

        boolean findGap = false;
        int currentSize = 0;
        int answer = 0;
        for (int i = 0; i < binaryList.size(); i++) {
            if (findGap) {
                if (binaryList.get(i) == 1) {
                    if (answer < currentSize) {
                        answer = currentSize;
                    }
                    currentSize = 0;
                } else {
                    currentSize += 1;
                }
            } else if (binaryList.get(i) == 1) {
                findGap = true;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] testInputs = {1041, 32, 9, 529};
        int[] answers = {5, 0, 2, 4};

        for (int i = 0; i < testInputs.length; i++) {
            int N = testInputs[i];
            int result = sol.solution(N);

            System.out.println("### TEST CASE " + (i+1) + " ###");
            System.out.println("- Solution: " + result);
            System.out.println("- Expected: " + answers[i]);
        }
    }
}