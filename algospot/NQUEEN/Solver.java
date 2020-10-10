import java.util.Scanner;
import java.lang.Integer;

public class Solver {
    private static int numSolutions = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = Integer.parseInt(sc.nextLine());

        for (int i = 0; i < T; i ++) {
            numSolutions = 0;
            int N = Integer.parseInt(sc.nextLine());
            System.out.println(solveNQueen(N));
        }

        sc.close();
    }

    private static int solveNQueen(int N) {
        int[] pos = new int[N];
        for (int row = 0; row < pos.length; row++) {
            pos[row] = -1;
        }
        searchComplete(0, pos);
        return numSolutions;
    }

    private static void searchComplete(int row, int[] pos) {
        int N = pos.length;
        if (row == N) {
            numSolutions ++;
            return;
        } 
        for (int col = 0; col < N; col ++) {
            if (isSafe(pos, row, col)) {
                pos[row] = col;
                searchComplete(row+1, pos);
            }
            pos[row] = -1;
        }
    }

    private static boolean isSafe(int[] pos, int row, int col) {
        // Check previous rows
		for(int r = 1; r <= row; r++){
			if (col - r >=0 && pos[row-r] == col-r) {
                return false;
            } 
			if (col + r < pos.length && pos[row-r] == col+r) {
                return false;
            }
        }
        // Check later rowss
		for (int r = row; r >= 0; r--) {
			if (pos[r] == col) return false;
		}
		return true;
    }
}