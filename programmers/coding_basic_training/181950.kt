// 문자열 반복해서 출력하기
// https://school.programmers.co.kr/learn/courses/30/lessons/181950

fun main(args: Array<String>) {
    val input = readLine()!!.split(' ')
    val s1 = input[0]
    val a = input[1]!!.toInt()

    repeat(a) {
        print(s1)
    }
}