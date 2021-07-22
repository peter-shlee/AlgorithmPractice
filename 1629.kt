import java.util.*

// 곱셈
// https://www.acmicpc.net/problem/1629

lateinit var dp: MutableMap<Long, Long>

fun main() {
    val (a, b, c) = input()
    println(solve(a, b, c))
}

fun input(): Triple<Long, Long, Long> {
    val reader = Scanner(System.`in`)
    val a = reader.nextLong()
    val b = reader.nextLong()
    val c = reader.nextLong()

    dp = mutableMapOf()
    dp[0] = 0
    dp[1] = a % c

    return Triple(a, b, c)
}

fun solve(a: Long, b: Long, c: Long): Long {
    dp[b]?.let {
        return it
    }

    dp[b] = (solve(a, b / 2, c) * solve(a, b - (b / 2), c)) % c

    return dp[b]!!
}
