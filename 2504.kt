// 괄호의 값
// https://www.acmicpc.net/problem/2504

fun main() {
    val brackets = input()
    println(solve(brackets))
}

fun input(): String = System.`in`.bufferedReader().readLine()

fun solve(brackets: String): Int {
    var depth = 0
    val tmpAnswers = MutableList(20) {1}
    val stack  = ArrayDeque<Char>()

    for (bracket in brackets) {
        when (bracket) {
            '(' -> {
                depth += 1
                stack.addLast(bracket)
            }
            '[' -> {
                depth += 1
                stack.addLast(bracket)
            }
            ')' -> {
                if (stack.isEmpty()) return 0
                if (stack.removeLast() == '(') {
                    if (tmpAnswers[depth - 1] == 1) {
                        tmpAnswers[depth - 1] = tmpAnswers[depth] * 2
                    } else {
                        tmpAnswers[depth - 1] += tmpAnswers[depth] * 2
                    }
                    tmpAnswers[depth] = 1
                    depth -= 1
                } else {
                    return 0
                }
            }
            ']' -> {
                if (stack.isEmpty()) return 0
                if (stack.removeLast() == '[') {
                    if (tmpAnswers[depth - 1] == 1) {
                        tmpAnswers[depth - 1] = tmpAnswers[depth] * 3
                    } else {
                        tmpAnswers[depth - 1] += tmpAnswers[depth] * 3
                    }
                    tmpAnswers[depth] = 1
                    depth -= 1
                } else {
                    return 0
                }
            }
        }
    }

    if (stack.isNotEmpty()) return 0

    return tmpAnswers[0]
}
