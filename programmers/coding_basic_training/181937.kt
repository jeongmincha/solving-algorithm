// n의 배수
// https://school.programmers.co.kr/learn/courses/30/lessons/181937

class Solution {
    fun solution(num: Int, n: Int): Int {
        return if(num % n == 0) 1 else 0
    }
}