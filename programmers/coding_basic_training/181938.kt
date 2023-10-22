// 두 수의 연산값 비교하기
// https://school.programmers.co.kr/learn/courses/30/lessons/181938

class Solution {
    fun solution(a: Int, b: Int): Int {
        var answer: Int = 0
        
        val x = (a.toString() + b.toString()).toInt()
        val y = 2 * a * b
        
        return maxOf(x, y)
    }
}