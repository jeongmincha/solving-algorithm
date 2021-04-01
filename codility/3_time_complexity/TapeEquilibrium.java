class TapeEquilibrium {
    public int solution(int[] A) {
        int[] prefixSums = new int[A.length];
        int[] suffixSums = new int[A.length];

        int prefixSum = 0;
        int suffixSum = 0;
        for (int i = 0; i < A.length; i++) {
            prefixSum += A[i];
            suffixSum += A[A.length - i - 1];
            prefixSums[i] = prefixSum;
            suffixSums[A.length - i - 1] = suffixSum;
        }

        int minDiff = Integer.MAX_VALUE;
        for (int i = 0; i < A.length-1; i++) {
            int diff = Math.abs(prefixSums[i] - (suffixSums[i] - A[i]));
            if (minDiff > diff) {
                minDiff = diff;
            }
        }
        return minDiff;
    }

    public static void main(String[] args) {
        TapeEquilibrium tapeEquilibrium = new TapeEquilibrium();
        int[][] testInputs = {{3,1,2,4,3}};
        int[] answers = {1};

        for (int i = 0; i < testInputs.length; i++) {
            int[] A = testInputs[i];
            int result = tapeEquilibrium.solution(A);

            System.out.println("### TEST CASE " + (i+1) + " ###");
            System.out.println("- Solution: " + result);
            System.out.println("- Expected: " + answers[i]);
        }
    }
}
