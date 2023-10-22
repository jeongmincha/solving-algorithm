// 문자열 섞기
// https://school.programmers.co.kr/learn/courses/30/lessons/181942

class Solution {
    fun solution(str1: String, str2: String): String {
        var answer: String = ""
        
        for (idx in 0 until str1.length) {
            answer += "${str1[idx]}${str2[idx]}"
        }
        
        return answer
    }
}