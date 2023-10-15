// 대소문자 바꿔서 출력하기
// https://school.programmers.co.kr/learn/courses/30/lessons/181949

fun main(args: Array<String>) {
    val s1 = readLine()!!
    
    for (c in s1) {
        if (c.isUpperCase()) {
            print(c.lowercaseChar())
        }
        if (c.isLowerCase()) {
            print(c.uppercaseChar())
        }
    }
}