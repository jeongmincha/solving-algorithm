// 부분 문자열인지 확인하기
// https://school.programmers.co.kr/learn/courses/30/lessons/181843

class Solution {
    fun solution(my_string: String, target: String): Int {
        var answer: Int = 0

        var target_idx = 0
        for (idx in 0 until my_string.length) {
            if (my_string[idx] == target[target_idx]) {
                target_idx += 1
            }
            if (target_idx == target.length) {
                answer = 1
                break
            }
        }
        
        return answer
    }
}