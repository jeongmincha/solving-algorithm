import java.util.ArrayList;
import java.util.Collections;
import java.util.Stack;

enum PointType {
    Start(0), End(1);

    private final int value;

    PointType(final int newValue) {
        value = newValue;
    }

    public int getValue() { return value; }
} 

class Point implements Comparable<Point>{
    int position;
    PointType type;

    public Point(int position, PointType start) {
        this.position = position;
        this.type = start;
    }

    public int getPosition() {
        return position;
    }

    public PointType getType() {
        return type;
    }

    @Override
    public int compareTo(Point o) {
        if (this.position < o.getPosition()) {
            return -1;
        } else if (this.position > o.getPosition()) {
            return 1;
        } else if (this.type.getValue() < o.getType().getValue()) {
            return -1;
        } else if (this.type.getValue() > o.getType().getValue()) {
            return 1;
        } else {
            return 0;
        }
    }
}

class NumberOfDiscIntersections {
    public int solution(int[] A) {
        ArrayList<Point> pointList = new ArrayList<>();

        for (int i = 0; i < A.length; i++) {
            pointList.add(new Point(i-A[i], PointType.Start));
            pointList.add(new Point(i+A[i], PointType.End));
        }

        Collections.sort(pointList);

        int answer = 0;
        Stack<Point> startPointStack = new Stack<>();
        for(int i = 0; i < pointList.size(); i++) {
            Point point = pointList.get(i);
            if (point.getType() == PointType.Start) {
                startPointStack.add(point);
            } else if (!startPointStack.isEmpty()) {
                startPointStack.pop();
                answer += startPointStack.size();
            }
        }

        if (answer > 10000000) {
            return -1;
        } else {
            return answer;
        }
    }

    public static void main(String[] args) {
        NumberOfDiscIntersections numberOfDiscIntersections = new NumberOfDiscIntersections();
        int[][] testInputs = {{1,5,2,1,4,0}, {1,1,1}};
        int[] answers = {11, 3};

        for (int i = 0; i < testInputs.length; i++) {
            int[] A = testInputs[i];
            int result = numberOfDiscIntersections.solution(A);

            System.out.println("### TEST CASE " + (i+1) + " ###");
            System.out.println("- Solution: " + result);
            System.out.println("- Expected: " + answers[i]);
        }
    }
}
