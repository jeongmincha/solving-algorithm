// 더 크게 합치기
// https://school.programmers.co.kr/learn/courses/30/lessons/181939

class Solution {
    fun solution(a: Int, b: Int): Int {
        var answer: Int = 0
        
        val x = (a.toString() + b.toString()).toInt()
        val y = (b.toString() + a.toString()).toInt()
        
        return maxOf(x, y)
    }
}