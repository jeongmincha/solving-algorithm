// 문자열 겹쳐쓰기
// https://school.programmers.co.kr/learn/courses/30/lessons/181943

class Solution {
    fun solution(my_string: String, overwrite_string: String, s: Int): String {
        var answer: String = ""
        
        my_string.forEachIndexed { idx, c -> 
            if (idx < s) {
                answer += c
            } else if (idx-s < overwrite_string.length) {
                answer += overwrite_string[idx-s]
            } else {
                answer += c
            }
        }
        
        return answer
    }
}