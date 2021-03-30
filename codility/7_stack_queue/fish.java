import java.util.Stack;

class Solution {
    public int solution(int[] A, int[] B) {
        Stack<Integer> downstreamFishes = new Stack<>();
        int aliveCount = 0;

        for (int i = 0; i < A.length; i++) {
            if (B[i] == 1)
                downstreamFishes.push(A[i]);
            else {
                while (!downstreamFishes.isEmpty()) {
                    int lastDownstreamFish = downstreamFishes.peek();
                    if (lastDownstreamFish > A[i])
                        break;
                    else
                        downstreamFishes.pop();
                }
                if (downstreamFishes.isEmpty())
                    aliveCount++;
            }
        }

        return aliveCount + downstreamFishes.size();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[][][] testCases = { { { 4, 3, 2, 1, 5 }, { 0, 1, 0, 0, 0 } } };
        int[] answers = { 2 };

        for (int i = 0; i < testCases.length; i++) {
            int[] A = testCases[i][0];
            int[] B = testCases[i][1];
            int result = sol.solution(A, B);

            System.out.println("### TEST CASE " + (i + 1) + " ###");
            System.out.println("Solution: " + result);
            System.out.println("Expected: " + answers[i]);
        }
    }
}