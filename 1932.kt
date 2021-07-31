import java.util.*
import kotlin.math.max

// 정수 삼각형
// https://www.acmicpc.net/problem/1932

var n = 0
val triangle = mutableListOf<List<Int>>()
val dp = mutableListOf<MutableList<Int>>()

fun main() {
    input()
    println(solve(0, 0))
}

fun input() {
    val reader = Scanner(System.`in`)
    n = reader.nextInt()
    reader.nextLine()
    for (i in 0 until n) {
        val nums = reader.nextLine().split(" ").map { it.toInt() }
        triangle.add(nums)
        dp.add(MutableList(nums.size) { -1 })
    }
}

fun solve(r: Int, c: Int): Int {
    if (r == n) return 0

    if (dp[r][c] != -1) return dp[r][c]

    dp[r][c] = max(solve(r + 1, c), solve(r + 1, c + 1)) + triangle[r][c]
    return dp[r][c]
}