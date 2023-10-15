// 덧셈식 출력하기
// https://school.programmers.co.kr/learn/courses/30/lessons/181947

fun main(args: Array<String>) {
    val (a, b) = readLine()!!.split(' ').map(String::toInt)
    println("$a + $b = ${a+b}")
}