// 뒤에서 5등 위로
// https://school.programmers.co.kr/learn/courses/30/lessons/181852

class Solution {
    fun solution(num_list: IntArray): IntArray {        
        num_list.sort()
        return num_list.copyOfRange(5, num_list.size)
    }
}